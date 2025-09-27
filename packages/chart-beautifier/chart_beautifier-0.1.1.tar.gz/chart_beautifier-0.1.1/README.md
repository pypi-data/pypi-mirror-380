# Chart Beautifier SDK

A Python SDK for creating beautiful and interactive charts.

## Installation

```bash
pip install chart-beautifier
```

## Quick Start

```python
from chart_beautifier import ChartBeautifierClient

# Initialize the client
client = ChartBeautifierClient(api_key="your_api_key")

# Create a chart
chart_data = {
    "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
    "datasets": [{
        "label": "Sales",
        "data": [12, 19, 3, 5, 2]
    }]
}

chart = client.create_chart(chart_data, chart_type="line")
print(f"Created chart: {chart['chart_id']}")
```

## Features

- 🎨 Beautiful chart generation
- 📊 Multiple chart types support
- 🔧 Easy-to-use Python API
- 🚀 Fast and reliable
- 📱 Responsive design

## API Reference

### ChartBeautifierClient

The main client class for interacting with the Chart Beautifier API.

#### Methods

- `create_chart(data, chart_type)`: Create a new chart
- `get_chart(chart_id)`: Retrieve a chart by ID
- `update_chart(chart_id, updates)`: Update an existing chart
- `delete_chart(chart_id)`: Delete a chart

## Development

### Setup

```bash
git clone https://github.com/yourusername/chart-beautifier.git
cd chart-beautifier
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black chart_beautifier/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
