# Engine AI Platform SDK

[![PyPI version](https://badge.fury.io/py/engineai.sdk.svg)](https://badge.fury.io/py/engineai.sdk)
[![Python versions](https://img.shields.io/pypi/pyversions/engineai.sdk.svg)](https://pypi.org/project/engineai.sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful Python library for building data-driven applications and interactive dashboards. The Engine AI Platform SDK empowers developers to transform raw data into compelling visualizations and insights with minimal effort.

## 🚀 Features

- **Extensive Widget Library**: Charts, tables, maps, tiles, and more
- **Flexible Layouts**: Grid systems, cards, tabs, and collapsible sections
- **Data Connectors**: Built-in support for DuckDB, Snowflake, and HTTP APIs
- **Interactive Components**: Buttons, selectors, search, and navigation
- **Time Series Support**: Advanced time-based visualizations with playback
- **Geographic Visualizations**: Maps with country-level data and styling
- **Command Line Interface**: Streamlined workflow for dashboard management

## 📋 Requirements

- Python 3.10 or higher

## 🛠️ Installation

Install the SDK from PyPI:

```bash
pip install engineai.sdk
```

Or use uv for faster installation:

```bash
uv add engineai.sdk
```

## 🎯 Quick Start

### 1. Create or select a workspace: Set up your organizational container (authentication will be handled automatically)
   ```bash
   engineai workspace create my-workspace "My Workspace"
   ```

### 2. Create an application: Set up a container for your dashboards
   ```bash
   engineai app create my-workspace my-app "My App"
   ```

### 3. Create a dashboard: Set up a dashboard
   ```bash
   engineai dashboard create my-workspace my-app first-dashboard "My First Dashboard"
   ```

### 4. Build Your Dashboard

Create a python file `dashboard.py` to customize your dashboard:

```python
"""My first dashboard using Engine AI SDK."""

import pandas as pd

from engineai.sdk.dashboard.dashboard import Dashboard
from engineai.sdk.dashboard.widgets import pie

data = pd.DataFrame(
    {
        "region": [
            "North America",
            "Europe",
            "Asia Pacific",
            "Latin America",
            "Africa",
        ],
        "sales": [45000, 32000, 28000, 15000, 8000],
    }
)

pie_widget = pie.Pie(
    data=data,
    title="Sales by Region - Q4 2024",
    series=pie.Series(
        category_column="region",  # This column defines the pie slices
        data_column="sales",  # This column defines the slice sizes
    ),
)

if __name__ == "__main__":
    Dashboard(
        workspace_slug="my-workspace",
        app_slug="my-app",
        slug="first-dashboard",
        content=pie_widget,
    )
```

### 2. Publish Your Dashboard

Deploy your dashboard to the Engine AI platform:

```bash
python dashboard.py
```
**Congratulations!** 🎉 You've successfully created your first interactive dashboard with the Engine AI SDK. This minimal example demonstrates how easy it is to get started with data visualization using the Engine AI platform.

## 📖 Documentation

- **[Official SDK Documentation](https://docs.engineai.com/sdk/getting_started/installation.html)** - Complete API reference and guides

## 📄 License

This project is licensed under the MIT License.

## 🤝 Support

- **Email**: support@engineai.com
- **Engine AI Documentation**: https://docs.engineai.com

---

Built by the Engine AI team
