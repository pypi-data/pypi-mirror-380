"""
GA4 Analytics API Client

A simple library for making raw Google Analytics 4 API calls.
All data processing should be handled in the consuming application.
"""

from datetime import datetime
from typing import List, Union

import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


class GA4Client:
    """
    A simple client for Google Analytics 4 API calls
    """

    def __init__(self, credentials_path: str, property_id: str, report_limit: int = 1000000):
        """
        Initialize GA4 Client

        Args:
            credentials_path: Path to Google Analytics service account JSON
            property_id: GA4 property ID
            report_limit: Maximum rows to fetch per report
        """
        self.credentials_path = credentials_path
        self.property_id = property_id
        self.report_limit = report_limit
        self.client = BetaAnalyticsDataClient.from_service_account_json(credentials_path)

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
            pandas.DataFrame: Raw report data (no processing applied)
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

        # Process response into DataFrame
        data = []
        for row in response.rows:
            dimension_values = [dim.value for dim in row.dimension_values]
            metric_values = [float(metric.value) for metric in row.metric_values]
            data.append(dimension_values + metric_values)

        columns = dimensions_list + metrics_list
        return pd.DataFrame(data, columns=columns)

    @staticmethod
    def load_email_campaign_data(url: str):
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