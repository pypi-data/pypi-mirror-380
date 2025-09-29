# GA4 Analytics Processor

A Python library for processing Google Analytics 4 data with built-in data transformations and channel grouping logic.

## Installation

```bash
pip install ga4-analytics-processor
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

# Fetch and process general report
df = processor.get_general_report(start_date, end_date)
print(df.head())
```

## Features

- Easy GA4 API integration
- Built-in data transformations and cleaning
- Channel grouping and campaign labeling
- Revenue reallocation logic
- Email campaign data integration
- Configurable data formatting

## Requirements

- Python 3.8+
- Google Analytics Data API credentials
- pandas, numpy, google-analytics-data

## License

MIT License