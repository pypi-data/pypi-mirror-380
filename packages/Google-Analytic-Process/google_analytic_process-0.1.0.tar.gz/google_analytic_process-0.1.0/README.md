# Google Analytics Process

A Python library for processing Google Analytics 4 data with built-in data transformations and channel grouping logic.

## Installation

```bash
pip install Google-Analytic-Process
```

## Quick Start

```python
from ga4_analytics import GA4Processor
from datetime import datetime, timedelta

# Initialize processor
processor = GA4Processor(
    credentials_path="/path/to/your/credentials.json",
    property_id="your_ga4_property_id"
)

# Define date range
end_date = datetime.now().date()
start_date = end_date - timedelta(days=7)

# Fetch and process general report with default dimensions/metrics
df = processor.get_general_report(start_date, end_date)

# Or specify custom dimensions and metrics
custom_dimensions = ["date", "sessionDefaultChannelGroup", "deviceCategory"]
custom_metrics = ["sessions", "totalRevenue", "transactions"]
df_custom = processor.get_general_report(
    start_date, end_date,
    dimensions=custom_dimensions,
    metrics=custom_metrics
)

# For completely custom reports with optional processing
df_raw = processor.get_custom_report(
    start_date, end_date,
    dimensions=custom_dimensions,
    metrics=custom_metrics,
    apply_processing=False  # Get raw data without transformations
)

print(df.head())
```

## Features

- Easy GA4 API integration
- **Flexible dimensions and metrics** - specify your own or use defaults
- **Custom report generation** - with optional data processing
- Built-in data transformations and cleaning
- Channel grouping and campaign labeling
- Revenue reallocation logic
- Email campaign data integration
- Configurable data formatting

## Features in v0.1.0

- ✅ **Custom dimensions and metrics** in `get_general_report()`
- ✅ **New `get_custom_report()` method** for full flexibility
- ✅ **Optional data processing** - get raw data or processed data
- ✅ **Easy GA4 API integration**

## Requirements

- Python 3.8+
- Google Analytics Data API credentials
- pandas, numpy, google-analytics-data

## License

MIT License