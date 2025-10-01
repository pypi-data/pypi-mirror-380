# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**SweetiePy** is a Python package for accessing and analyzing Type 1 diabetes data from a DIY Loop system stored in MongoDB Atlas. The primary focus is CGM (Continuous Glucose Monitor) data analysis and correlation with pump settings to identify patterns and optimize diabetes management.

## Key Commands

### Development Commands
```bash
# Environment setup (uses uv package manager)
uv sync                                    # Install all dependencies
uv pip install -e .                       # Install package in editable mode for development

# Module testing
uv run python -m sweetiepy.connection.mongodb    # Test database connection
uv run python -m sweetiepy.data.cgm             # Test CGM data access  
uv run python -m sweetiepy.data.pump            # Test pump data access
uv run python -m sweetiepy.data.merged          # Test merged CGM+pump data
uv run python -m sweetiepy.utils.debug          # Debug connection issues

# Usage examples
uv run python dev/usage_example.py              # Basic CGM data analysis (3 months)
uv run python dev/merged_data_example.py        # CGM + pump settings correlation
uv run python dev/pump_usage_example.py         # Pump treatment data analysis

# Interactive exploration
uv run marimo edit dev/exploratory/analysis.py  # Start marimo notebook for data exploration
```

### Build and Publish Commands
```bash
# Update version in pyproject.toml first
uv run python -m build                          # Build package for PyPI
uv run python publish.py                        # Publish to PyPI (requires TWINE_PASSWORD in .env)
```

## Architecture Overview

### Core Data Access Pattern
The architecture follows a **three-layer data access pattern**:

1. **Connection Layer** (`connection/mongodb.py`) - Handles MongoDB authentication and database connections
2. **Data Access Layer** (`data/`) - Specialized classes for different data types:
   - `CGMDataAccess` - Continuous glucose monitor readings
   - `PumpDataAccess` - Insulin pump treatments (bolus, basal, carbs)
   - `MergedDataAccess` - **Key innovation**: Time-synchronized CGM + pump settings correlation
3. **Context Manager Support** - All data access classes support `with` statements for automatic connection management

### MongoDB Collections Schema
The `myCGMitc` database contains:
- **`entries`** - 243K+ CGM readings (primary analysis data)
- **`treatments`** - Insulin doses, basal adjustments, carb entries
- **`profile`** - Pump settings schedules (basal rates, carb ratios, ISF)
- **`settings`** - Loop system configuration
- **`food`**, **`devicestatus`**, **`activity`** - Supporting data

### Time-Synchronized Analysis (Core Innovation)
The `MergedDataAccess` module is the architectural centerpiece:
- Synchronizes each CGM reading with active pump settings at that timestamp
- Enables correlation analysis: how basal rates/carb ratios/ISF affect glucose outcomes
- Provides temporal context with recent insulin/carb treatments
- Powers pattern analysis and settings optimization insights

## Development Patterns

### Database Connection Pattern
```python
# Context manager approach (recommended)
with CGMDataAccess() as cgm:
    df = cgm.get_dataframe_for_period('last_week')
    analysis = cgm.analyze_dataframe(df)

# Manual connection management
cgm = CGMDataAccess()
cgm.connect()
try:
    df = cgm.get_dataframe_for_period('last_week')
finally:
    cgm.disconnect()
```

### Time Period Queries
Standard periods: `'last_24h'`, `'last_week'`, `'last_month'`, `'last_3_months'`

### Data Analysis Workflow
1. **Data Retrieval** - Use specialized access classes with predefined periods
2. **DataFrame Conversion** - PyArrow-backed pandas DataFrames for performance
3. **Time-Series Analysis** - Focus on weeks/months, not entire 243K+ dataset
4. **Pattern Discovery** - Hourly/daily patterns, correlations with settings
5. **Visualization** - marimo notebooks for interactive exploration

### Merged Data Correlation Analysis
```python
with MergedDataAccess() as merged:
    # Each CGM reading includes active pump settings
    df = merged.get_merged_cgm_and_settings(days=7)
    
    # Analyze how settings affect glucose outcomes
    analysis = merged.analyze_settings_correlation(df)
    
    # Include recent treatment context
    df_with_context = merged.get_merged_with_recent_treatments(days=3, lookback_hours=4)
```

## Environment Configuration

### Required Environment Variables (.env file)
```bash
MONGODB_USERNAME=your_username
MONGODB_PW=your_password
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority
MONGODB_DATABASE=myCGMitc
TWINE_PASSWORD=pypi-token-for-publishing  # Optional: for PyPI publishing
```

**Important**: Keep `<username>` and `<password>` placeholders in URI - they're automatically replaced by the code.

### Python Environment
- **Python 3.12+** required
- **uv package manager** preferred for dependency management
- **PyArrow backend** enabled for pandas performance optimization
- Virtual environment located in `python/` folder (per user preference)

## Package Structure

```
src/sweetiepy/
├── connection/         # MongoDB connectivity
│   └── mongodb.py     # Connection management, authentication
├── data/              # Core data access modules  
│   ├── cgm.py        # CGM readings, time-range queries, basic analysis
│   ├── pump.py       # Pump treatments, insulin/carb data, settings profiles
│   └── merged.py     # CGM+pump correlation analysis (key innovation)
└── utils/
    └── debug.py      # Connection debugging utilities

dev/                   # Development scripts and examples
├── exploratory/      # marimo notebooks for data exploration
├── usage_example.py  # Complete CGM data workflow demonstration
├── merged_data_example.py  # Settings correlation analysis example
└── pump_usage_example.py   # Pump data analysis patterns

notes/                # Analysis documentation and implementation plans
tests/                # Test modules for connection verification
```

## Key Development Concepts

### Time-Series Focus
Analyze manageable time periods (weeks/months) rather than the full 243K+ reading dataset. The system is optimized for temporal pattern analysis, not bulk data processing.

### PyArrow Performance
All DataFrames use PyArrow backend for efficient processing of diabetes time-series data:
```python
pd.options.mode.dtype_backend = "pyarrow"
```

### Professional Code Standards
- **Type hints** on all functions and methods
- **Comprehensive docstrings** following Google/NumPy style
- **Context manager support** for resource management
- **Error handling** with informative messages
- **Data validation** and quality checks

### Analysis Methodology
The project follows documented analysis patterns in `notes/analysis_patterns.md`:
- CGM-focused time-series analysis for pattern discovery
- Settings correlation analysis for treatment optimization
- Statistical analysis with time-in-range calculations
- Visualization approaches for pattern identification

## Security and Data Handling

- **Environment-based configuration** - no hardcoded credentials
- **Read-only database access** patterns
- **Secure credential management** - .env file gitignored
- **Personal health data** - treat all data as sensitive PHI

## Testing and Validation

- **Connection testing** via module execution (`python -m sweetiepy.connection.mongodb`)
- **Data quality validation** - missing values, outliers, timestamp integrity
- **Analysis validation** - statistical checks and correlation verification

## Future Development Context

The codebase is designed for:
- **Pattern analysis** and **treatment correlation** (current focus)
- **Machine learning integration** for predictive modeling (future)
- **Settings optimization** recommendations (future)
- **Integration with other diabetes management tools** (future)

Key architectural decisions support both current analysis needs and future ML/AI capabilities.