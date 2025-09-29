"""
GA4 Analytics Data Processor

A comprehensive library for fetching and processing Google Analytics 4 data
with built-in transformations, channel grouping, and data cleaning.
"""

import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

import numpy as np
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


class GA4Processor:
    """
    A processor for Google Analytics 4 data with built-in transformations
    """

    def __init__(self, credentials_path: str, property_id: str, report_limit: int = 1000000):
        """
        Initialize GA4 Processor

        Args:
            credentials_path: Path to Google Analytics service account JSON
            property_id: GA4 property ID
            report_limit: Maximum rows to fetch per report
        """
        self.credentials_path = credentials_path
        self.property_id = property_id
        self.report_limit = report_limit
        self.client = BetaAnalyticsDataClient.from_service_account_json(credentials_path)

        # I2 product keywords for campaign labeling
        self.i2_keywords = ["i2", "i-2", "i 2", "I-2", "I2", "I 2"]

    def run_report(self, dimensions_list: List[str], metrics_list: List[str],
                   start_date: Union[str, datetime], end_date: Union[str, datetime]) -> pd.DataFrame:
        """
        Run Google Analytics 4 report with specified dimensions and metrics

        Args:
            dimensions_list: List of dimension names
            metrics_list: List of metric names
            start_date: Start date for the report
            end_date: End date for the report

        Returns:
            pandas.DataFrame: Report data
        """
        # Convert dates to string format if needed
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = str(start_date)

        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = str(end_date)

        # Create dimension and metric objects
        dimensions = [Dimension(name=dim) for dim in dimensions_list]
        metrics = [Metric(name=metric) for metric in metrics_list]

        # Build request
        request = RunReportRequest(
            property=f"properties/{self.property_id}",
            dimensions=dimensions,
            metrics=metrics,
            date_ranges=[DateRange(start_date=start_date_str, end_date=end_date_str)],
            limit=self.report_limit,
            offset=0
        )

        # Execute request
        response = self.client.run_report(request)

        # Process response
        data = []
        for row in response.rows:
            dimension_values = [dim.value for dim in row.dimension_values]
            metric_values = [float(metric.value) for metric in row.metric_values]
            data.append(dimension_values + metric_values)

        columns = dimensions_list + metrics_list
        return pd.DataFrame(data, columns=columns)

    def update_channel_groups(self, df: pd.DataFrame) -> pd.DataFrame:
        """Update channel groups based on business logic"""
        df = df.copy()
        df['CustomChannel'] = np.where(
            df['sessionDefaultChannelGroup'].isin(['Cross-network', 'Paid Shopping']),
            'Paid Search',
            df['sessionDefaultChannelGroup']
        )

        # Update for video campaigns
        video_condition = (
            df['sessionCampaignName'].str.lower().str.contains('video', na=False) &
            (df['CustomChannel'] == 'Paid Search')
        )
        df.loc[video_condition, 'CustomChannel'] = 'Paid Video'

        return df

    def label_campaigns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Label campaigns based on I2 product filters"""
        df = df.copy()

        def categorize_campaign(row):
            if row['CustomChannel'] in ['Paid Search', 'Paid Social']:
                campaign_name = str(row['sessionCampaignName'])
                ad_group_name = str(row.get('sessionGoogleAdsAdGroupName', ''))

                for keyword in self.i2_keywords:
                    if keyword in campaign_name:
                        return 'I2 Campaign'
                    elif keyword in ad_group_name:
                        return 'I2 Ad Group'
            return 'Other Campaign'

        df['LabelCampaign'] = df.apply(categorize_campaign, axis=1)
        return df

    def update_channels_and_label(self, df: pd.DataFrame) -> pd.DataFrame:
        """Combined function to update channels and labels efficiently"""
        df = self.update_channel_groups(df)
        df = self.label_campaigns(df)
        return df

    @staticmethod
    def format_dataframe(df: pd.DataFrame, config: Dict[str, Union[str, int]]) -> None:
        """
        Format DataFrame columns based on configuration

        Args:
            df: DataFrame to format (modified in place)
            config: Dictionary mapping column names to format types
        """
        for column, operation in config.items():
            if column not in df.columns:
                continue

            if operation == 'int':
                df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)
            elif isinstance(operation, int):
                df[column] = pd.to_numeric(df[column], errors='coerce').round(operation)

    @staticmethod
    def reallocate_unassigned_revenue(df: pd.DataFrame) -> pd.DataFrame:
        """Reallocate revenue from unassigned channels proportionally"""
        df = df.copy()

        unassigned_mask = df["DefaultChannel"] != "Unassigned"
        total_revenue_assigned = df[unassigned_mask]["TotalRevenue"].sum()
        sessions_assigned = df[unassigned_mask]["Sessions"].sum()
        unassigned_revenue = df[df["DefaultChannel"] == "Unassigned"]["TotalRevenue"].sum()

        if total_revenue_assigned > 0 and sessions_assigned > 0:
            revenue_per_session = unassigned_revenue / sessions_assigned
            df.loc[unassigned_mask, "TotalRevenue"] += (
                df[unassigned_mask]["Sessions"] * revenue_per_session
            )

        df.loc[df["DefaultChannel"] == "Unassigned", "TotalRevenue"] = 0
        df['TotalRevenue'] = df['TotalRevenue'].round(2)
        return df

    def process_general_report(self, df: pd.DataFrame, email_campaign_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Process GA4 general report data with all transformations

        Args:
            df: Raw GA4 data
            email_campaign_df: Optional email campaign mapping data

        Returns:
            pandas.DataFrame: Processed data
        """
        df = df.copy()

        # Apply channel and label updates
        df = self.update_channels_and_label(df)

        # Rename columns
        rename_mapping = {
            'date': 'Date',
            'streamName': 'StreamName',
            'sessionDefaultChannelGroup': 'DefaultChannel',
            'sessionCampaignName': 'CampaignName',
            'sessionGoogleAdsAdGroupName': 'AdGroup',
            'deviceCategory': 'Device',
            'newVsReturning': 'UserType',
            'countryId': 'CountryCode',
            'sessions': 'Sessions',
            'transactions': 'Transactions',
            'totalUsers': 'TotalUsers',
            'totalRevenue': 'TotalRevenue',
            'engagementRate': 'EngagementRate'
        }
        df = df.rename(columns=rename_mapping)

        # Calculate derived metrics
        df['Date'] = pd.to_datetime(df['Date'])
        df['BounceRate'] = 1 - df['EngagementRate']
        df['Source'] = 'GA4'
        df['UserType'] = df['UserType'].replace(['(not set)', ''], 'new')

        # Merge with email campaign data if available
        if email_campaign_df is not None:
            df = df.merge(
                email_campaign_df[['CampaignName', 'EmailCampaignName']],
                on='CampaignName',
                how='left'
            ).fillna("no value")
        else:
            df['EmailCampaignName'] = "no value"

        # Clean data
        df.fillna(0, inplace=True)
        df.replace([np.inf, -np.inf], 0, inplace=True)

        # Format numeric columns
        config = {
            'Sessions': 'int', 'Transactions': 'int',
            'TotalRevenue': 2, 'TotalUsers': 'int',
            'BounceRate': 2, 'EngagementRate': 2
        }
        self.format_dataframe(df, config)

        # Reallocate unassigned revenue
        df = self.reallocate_unassigned_revenue(df)

        return df

    def get_general_report(self, start_date: Union[str, datetime], end_date: Union[str, datetime],
                          dimensions: Optional[List[str]] = None, metrics: Optional[List[str]] = None,
                          email_campaign_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Get processed GA4 general report data with flexible dimensions and metrics

        Args:
            start_date: Start date for the report
            end_date: End date for the report
            dimensions: List of GA4 dimensions (optional, uses defaults if not provided)
            metrics: List of GA4 metrics (optional, uses defaults if not provided)
            email_campaign_df: Optional email campaign mapping data

        Returns:
            pandas.DataFrame: Processed GA4 general report
        """
        # Use default dimensions and metrics if not provided
        if dimensions is None:
            dimensions = [
                "date", "streamName", "sessionDefaultChannelGroup", "sessionCampaignName",
                "sessionGoogleAdsAdGroupName", 'deviceCategory', 'newVsReturning', "countryId"
            ]

        if metrics is None:
            metrics = [
                "sessions", "transactions", "totalUsers", "totalRevenue", 'engagementRate'
            ]

        # Fetch raw data
        df_raw = self.run_report(dimensions, metrics, start_date, end_date)

        # Process and return
        return self.process_general_report(df_raw, email_campaign_df)

    def get_custom_report(self, start_date: Union[str, datetime], end_date: Union[str, datetime],
                         dimensions: List[str], metrics: List[str],
                         apply_processing: bool = True, email_campaign_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Get a custom GA4 report with specified dimensions and metrics

        Args:
            start_date: Start date for the report
            end_date: End date for the report
            dimensions: List of GA4 dimensions
            metrics: List of GA4 metrics
            apply_processing: Whether to apply standard processing (channel grouping, etc.)
            email_campaign_df: Optional email campaign mapping data

        Returns:
            pandas.DataFrame: GA4 report data
        """
        # Fetch raw data
        df_raw = self.run_report(dimensions, metrics, start_date, end_date)

        # Apply processing if requested
        if apply_processing:
            return self.process_general_report(df_raw, email_campaign_df)
        else:
            return df_raw

    def get_ads_report(self, start_date: Union[str, datetime], end_date: Union[str, datetime]) -> pd.DataFrame:
        """
        Get processed GA4 ads report data

        Args:
            start_date: Start date for the report
            end_date: End date for the report

        Returns:
            pandas.DataFrame: Processed GA4 ads report
        """
        # Define ads report dimensions and metrics
        dimensions_ads = [
            'date', 'sessionDefaultChannelGroup', 'sessionCampaignName'
        ]
        metrics_ads = [
            'sessions', 'transactions', 'totalRevenue', 'advertiserAdClicks',
            'advertiserAdCost', 'advertiserAdImpressions', 'advertiserAdCostPerClick',
            'returnOnAdSpend', 'sessionConversionRate', 'totalUsers', 'newUsers', 'engagedSessions'
        ]

        # Fetch raw data
        df_raw = self.run_report(dimensions_ads, metrics_ads, start_date, end_date)

        # Process ads data
        df = df_raw.copy()
        df = self.update_channel_groups(df)

        # Determine I2 label using regex
        df['LabelCampaign'] = df['sessionCampaignName'].apply(self._determine_i2_label)

        # Rename columns for ads
        rename_mapping = {
            'date': 'Date',
            'sessionDefaultChannelGroup': 'DefaultChannel',
            'sessionCampaignName': 'CampaignName',
            'sessions': 'Sessions',
            'transactions': 'Transactions',
            'totalRevenue': 'TotalRevenue',
            'advertiserAdClicks': 'TotalClicks',
            'advertiserAdCost': 'TotalAdCost',
            'advertiserAdImpressions': 'TotalImpressions',
            'advertiserAdCostPerClick': 'CPC',
            'returnOnAdSpend': 'ROAS',
            'sessionConversionRate': 'SessionConversionRate',
            'totalUsers': 'TotalUsers',
            'newUsers': 'NewUsers',
            'engagedSessions': 'EngagedSessions'
        }
        df = df.rename(columns=rename_mapping)

        # Calculate additional metrics
        df['Date'] = pd.to_datetime(df['Date'])
        df["CTR"] = (df["TotalClicks"] / df["TotalImpressions"]) * 100
        df["CPM"] = (df["TotalAdCost"] / df["TotalImpressions"]) * 1000

        # Clean data
        df.fillna(0, inplace=True)
        df.replace([np.inf, -np.inf], 0, inplace=True)

        return df

    def _determine_i2_label(self, campaign_name: str) -> str:
        """Determine if campaign is I-2 related using regex"""
        regex_pattern = r"\b(" + "|".join(map(re.escape, self.i2_keywords)) + r")\b"

        if re.search(regex_pattern, str(campaign_name), re.IGNORECASE):
            return 'I-2 only'
        return 'Everything else'

    @staticmethod
    def validate_dataframe(df: pd.DataFrame, required_columns: List[str], name: str) -> bool:
        """Validate that DataFrame has required columns"""
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"{name} missing columns: {missing}")
        return True

    @staticmethod
    def load_email_campaign_data(url: str) -> Optional[pd.DataFrame]:
        """
        Load email campaign mapping data from URL

        Args:
            url: URL to CSV data source

        Returns:
            DataFrame with email campaign mappings or None if failed
        """
        try:
            df_email = pd.read_csv(
                url,
                usecols=[0, 2, 3],
                names=['Date', 'CampaignName', 'EmailCampaignName'],
                header=0
            )
            return df_email
        except Exception as e:
            print(f"Warning: Could not load email campaign data: {e}")
            return None