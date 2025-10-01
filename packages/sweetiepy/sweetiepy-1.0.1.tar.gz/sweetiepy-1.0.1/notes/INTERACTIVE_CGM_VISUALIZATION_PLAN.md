# Interactive CGM Visualization Project Plan

This document outlines a comprehensive plan for creating an interactive CGM visualization that overlays blood glucose data with pump treatments. The project uses the existing sweetiepy package as a data source.

## Project Overview

**Goal**: Create an interactive web-based visualization showing:
- **Stage 1**: 24-hour CGM data with overlaid treatment dots (bolus, carbs, corrections)
- **Stage 2**: Multi-day overlay with time-aligned patterns  
- **Stage 3**: Advanced analytics and pattern recognition

## Project Setup

```bash
# Create new project directory
mkdir cgm-visualization
cd cgm-visualization

# Initialize with uv
uv init --name cgm-visualization

# Add dependencies
uv add sweetiepy
uv add plotly
uv add dash
uv add pandas
uv add python-dotenv
```

## Project Structure

```
cgm-visualization/
├── .env                    # MongoDB credentials (copy from sweetiepy)
├── app.py                  # Main Dash app
├── components/
│   ├── __init__.py
│   ├── cgm_chart.py       # Main CGM chart component
│   ├── treatment_overlay.py # Treatment dots overlay
│   └── controls.py        # Date/time controls
├── data/
│   ├── __init__.py
│   ├── cgm_loader.py      # CGM data loading
│   └── treatment_loader.py # Treatment data loading
├── utils/
│   ├── __init__.py
│   ├── colors.py          # Color schemes
│   └── formatting.py     # Data formatting helpers
└── README.md
```

---

# Stage 1: 24-Hour CGM + Treatment Overlay

## Core Implementation Files

### `data/cgm_loader.py`

```python
from sweetiepy.data.cgm import CGMDataAccess
from datetime import datetime, timedelta
import pandas as pd

def get_cgm_data_24h():
    """Get last 24 hours of CGM data using sweetiepy."""
    with CGMDataAccess() as cgm:
        df = cgm.get_dataframe_for_period('last_24h')
    return df

def get_cgm_data_custom(hours=24):
    """Get CGM data for custom hours."""
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=hours)
    
    with CGMDataAccess() as cgm:
        df = cgm.get_dataframe_for_period('custom', start_time, end_time)
    return df
```

### `data/treatment_loader.py`

```python
from sweetiepy.data.pump import PumpDataAccess
from datetime import datetime, timedelta
import pandas as pd

def get_treatments_24h():
    """Get last 24 hours of treatment data."""
    with PumpDataAccess() as pump:
        # Get different treatment types
        bolus_data = pump.get_bolus_data(days=1)
        carb_data = pump.get_carb_data(days=1) 
        basal_data = pump.get_basal_data(days=1)
        
        # Convert to DataFrames
        treatments = []
        
        for treatment in bolus_data:
            treatments.append({
                'timestamp': pd.to_datetime(treatment['timestamp']),
                'type': 'Correction Bolus',
                'value': treatment.get('insulin', 0),
                'units': 'U',
                'color': '#FF4444',
                'details': f"{treatment.get('insulin', 0)} units insulin"
            })
            
        for treatment in carb_data:
            treatments.append({
                'timestamp': pd.to_datetime(treatment['timestamp']),
                'type': 'Carb Correction', 
                'value': treatment.get('carbs', 0),
                'units': 'g',
                'color': '#44FF44',
                'details': f"{treatment.get('carbs', 0)}g carbs + {treatment.get('insulin', 0)}U insulin"
            })
            
        return pd.DataFrame(treatments)

def get_treatments_custom(hours=24):
    """Get treatment data for custom time period."""
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=hours)
    
    with PumpDataAccess() as pump:
        # Use the general get_treatments method with custom date range
        all_treatments = pump.get_treatments(
            start_date=start_time,
            end_date=end_time,
            limit=1000
        )
        
        treatments = []
        
        for treatment in all_treatments:
            timestamp = pd.to_datetime(treatment['timestamp'])
            event_type = treatment.get('eventType', 'Unknown')
            
            if event_type == 'Correction Bolus':
                treatments.append({
                    'timestamp': timestamp,
                    'type': 'Correction Bolus',
                    'value': treatment.get('insulin', 0),
                    'units': 'U',
                    'color': '#FF4444',
                    'details': f"{treatment.get('insulin', 0)} units insulin"
                })
            elif event_type == 'Carb Correction':
                carbs = treatment.get('carbs', 0)
                insulin = treatment.get('insulin', 0)
                treatments.append({
                    'timestamp': timestamp,
                    'type': 'Carb Correction',
                    'value': carbs,
                    'units': 'g',
                    'color': '#44FF44',
                    'details': f"{carbs}g carbs" + (f" + {insulin}U insulin" if insulin > 0 else "")
                })
            elif event_type == 'Temp Basal':
                treatments.append({
                    'timestamp': timestamp,
                    'type': 'Temp Basal',
                    'value': treatment.get('rate', 0),
                    'units': 'U/hr',
                    'color': '#4444FF',
                    'details': f"{treatment.get('rate', 0)} U/hr for {treatment.get('duration', 0)} min"
                })
        
        return pd.DataFrame(treatments)
```

### `components/cgm_chart.py`

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_cgm_chart(cgm_df, treatments_df):
    """Create interactive CGM chart with treatment overlay."""
    
    fig = go.Figure()
    
    # Add CGM line
    fig.add_trace(go.Scatter(
        x=cgm_df['datetime'],
        y=cgm_df['sgv'],
        mode='lines+markers',
        name='Glucose',
        line=dict(color='#2196F3', width=2),
        marker=dict(size=3),
        hovertemplate='<b>%{y} mg/dL</b><br>%{x}<extra></extra>'
    ))
    
    # Add treatment dots
    if not treatments_df.empty:
        for treatment_type in treatments_df['type'].unique():
            treatment_subset = treatments_df[treatments_df['type'] == treatment_type]
            
            # Find corresponding CGM values for y-positioning
            treatment_y_values = []
            for timestamp in treatment_subset['timestamp']:
                # Find closest CGM reading
                time_diffs = (cgm_df['datetime'] - timestamp).abs()
                if len(time_diffs) > 0:
                    closest_idx = time_diffs.idxmin()
                    treatment_y_values.append(cgm_df.loc[closest_idx, 'sgv'])
                else:
                    treatment_y_values.append(150)  # Default if no CGM data
            
            fig.add_trace(go.Scatter(
                x=treatment_subset['timestamp'],
                y=treatment_y_values,
                mode='markers',
                name=treatment_type,
                marker=dict(
                    size=12,
                    color=treatment_subset['color'].iloc[0],
                    symbol='circle',
                    line=dict(width=2, color='white')
                ),
                customdata=treatment_subset['details'].tolist(),
                hovertemplate='<b>%{fullData.name}</b><br>%{customdata}<br>%{x}<extra></extra>',
                showlegend=True
            ))
    
    # Add target range shading
    fig.add_hrect(y0=70, y1=180, 
                  fillcolor="rgba(76, 175, 80, 0.1)", 
                  line_width=0, 
                  annotation_text="Target Range")
    
    # Add reference lines
    fig.add_hline(y=70, line_dash="dash", line_color="red", opacity=0.5)
    fig.add_hline(y=180, line_dash="dash", line_color="orange", opacity=0.5)
    
    # Update layout
    fig.update_layout(
        title='24-Hour CGM with Treatment Overlay',
        xaxis_title='Time',
        yaxis_title='Glucose (mg/dL)',
        hovermode='closest',
        height=600,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left", 
            x=0.01
        )
    )
    
    return fig
```

### `app.py` - Main Dash App

```python
import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
from data.cgm_loader import get_cgm_data_24h, get_cgm_data_custom
from data.treatment_loader import get_treatments_24h, get_treatments_custom
from components.cgm_chart import create_cgm_chart

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive CGM Dashboard", style={'text-align': 'center'}),
    
    # Controls
    html.Div([
        html.Label("Time Range:"),
        dcc.Dropdown(
            id='time-range-dropdown',
            options=[
                {'label': 'Last 6 Hours', 'value': 6},
                {'label': 'Last 12 Hours', 'value': 12},
                {'label': 'Last 24 Hours', 'value': 24},
                {'label': 'Last 48 Hours', 'value': 48}
            ],
            value=24,
            style={'width': '200px', 'display': 'inline-block'}
        ),
        html.Button("Refresh Data", id="refresh-button", n_clicks=0,
                   style={'margin-left': '20px'})
    ], style={'padding': '20px', 'text-align': 'center'}),
    
    # Main chart
    dcc.Graph(id='cgm-chart', style={'height': '600px'}),
    
    # Treatment summary
    html.Div(id='treatment-summary', style={'padding': '20px'}),
    
    # Auto refresh every 5 minutes
    dcc.Interval(id='interval-component', interval=5*60*1000, n_intervals=0)
])

@callback(
    [Output('cgm-chart', 'figure'),
     Output('treatment-summary', 'children')],
    [Input('time-range-dropdown', 'value'),
     Input('refresh-button', 'n_clicks'),
     Input('interval-component', 'n_intervals')]
)
def update_chart(hours, refresh_clicks, n_intervals):
    # Load data
    cgm_df = get_cgm_data_custom(hours)
    treatments_df = get_treatments_custom(hours)
    
    # Create chart
    fig = create_cgm_chart(cgm_df, treatments_df)
    
    # Create treatment summary
    if not treatments_df.empty:
        treatment_counts = treatments_df['type'].value_counts()
        summary_text = html.Div([
            html.H4("Treatment Summary"),
            html.Ul([
                html.Li(f"{treatment_type}: {count}")
                for treatment_type, count in treatment_counts.items()
            ])
        ])
    else:
        summary_text = html.P("No treatments in selected time range")
    
    return fig, summary_text

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
```

### `utils/colors.py`

```python
# Color schemes for different treatment types
TREATMENT_COLORS = {
    'Correction Bolus': '#FF4444',      # Red
    'Carb Correction': '#44FF44',       # Green  
    'Temp Basal': '#4444FF',            # Blue
    'Site Change': '#FF44FF',           # Magenta
    'Suspend Pump': '#FFAA44',          # Orange
    'Temporary Override': '#44FFFF'     # Cyan
}

GLUCOSE_COLORS = {
    'low': '#FF4444',        # Red for <70
    'normal': '#44FF44',     # Green for 70-180
    'high': '#FFAA44',       # Orange for 180-250
    'very_high': '#FF0000'   # Dark red for >250
}

def get_glucose_color(glucose_value):
    """Return color based on glucose value."""
    if glucose_value < 70:
        return GLUCOSE_COLORS['low']
    elif glucose_value <= 180:
        return GLUCOSE_COLORS['normal']
    elif glucose_value <= 250:
        return GLUCOSE_COLORS['high']
    else:
        return GLUCOSE_COLORS['very_high']
```

---

# Stage 2: Multi-Day Time-Aligned Overlay

## Enhanced Data Loading

### `data/multi_day_loader.py`

```python
from sweetiepy.data.cgm import CGMDataAccess
from datetime import datetime, timedelta
import pandas as pd

def get_multi_day_aligned_data(days=7):
    """Get multiple days of CGM data aligned by time of day."""
    
    with CGMDataAccess() as cgm:
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        df = cgm.get_dataframe_for_period('custom', start_time, end_time)
    
    if df.empty:
        return df
    
    # Add time-alignment columns
    df['time_of_day'] = df['datetime'].dt.time
    df['minutes_since_midnight'] = (
        df['datetime'].dt.hour * 60 + df['datetime'].dt.minute
    )
    df['date_only'] = df['datetime'].dt.date
    df['days_ago'] = (end_time.date() - df['date_only']).dt.days
    
    return df

def create_aligned_traces(df):
    """Create separate traces for each day, aligned by time."""
    traces_data = []
    
    if df.empty:
        return traces_data
    
    for days_ago in sorted(df['days_ago'].unique()):
        day_data = df[df['days_ago'] == days_ago].copy()
        
        if day_data.empty:
            continue
        
        # Create normalized datetime for x-axis (today's date + time of day)
        today = datetime.now().date()
        day_data['normalized_datetime'] = pd.to_datetime(
            today.strftime('%Y-%m-%d') + ' ' + 
            day_data['datetime'].dt.strftime('%H:%M:%S')
        )
        
        opacity = 1.0 if days_ago == 0 else 0.3  # Current day bold, others faded
        line_width = 3 if days_ago == 0 else 1
        
        traces_data.append({
            'data': day_data,
            'days_ago': days_ago,
            'opacity': opacity,
            'line_width': line_width,
            'name': 'Today' if days_ago == 0 else f'{days_ago} days ago'
        })
    
    return traces_data

def get_multi_day_treatments(days=7):
    """Get treatments for multiple days, organized by day."""
    from sweetiepy.data.pump import PumpDataAccess
    
    with PumpDataAccess() as pump:
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        
        all_treatments = pump.get_treatments(
            start_date=start_time,
            end_date=end_time,
            limit=5000
        )
        
        treatments_by_day = {}
        
        for treatment in all_treatments:
            timestamp = pd.to_datetime(treatment['timestamp'])
            date_key = timestamp.date()
            days_ago = (end_time.date() - date_key).days
            
            if days_ago not in treatments_by_day:
                treatments_by_day[days_ago] = []
            
            # Normalize timestamp to today for alignment
            today = datetime.now().date()
            normalized_time = datetime.combine(today, timestamp.time())
            
            event_type = treatment.get('eventType', 'Unknown')
            
            treatment_data = {
                'timestamp': timestamp,
                'normalized_timestamp': normalized_time,
                'type': event_type,
                'days_ago': days_ago
            }
            
            if event_type == 'Correction Bolus':
                treatment_data.update({
                    'value': treatment.get('insulin', 0),
                    'units': 'U',
                    'color': '#FF4444',
                    'details': f"{treatment.get('insulin', 0)} units insulin"
                })
            elif event_type == 'Carb Correction':
                carbs = treatment.get('carbs', 0)
                insulin = treatment.get('insulin', 0)
                treatment_data.update({
                    'value': carbs,
                    'units': 'g',
                    'color': '#44FF44',
                    'details': f"{carbs}g carbs" + (f" + {insulin}U insulin" if insulin > 0 else "")
                })
            
            treatments_by_day[days_ago].append(treatment_data)
        
        return treatments_by_day
```

### `components/multi_day_chart.py`

```python
import plotly.graph_objects as go
from utils.colors import TREATMENT_COLORS

def create_multi_day_chart(aligned_traces, treatments_by_day=None):
    """Create multi-day aligned CGM chart."""
    
    fig = go.Figure()
    
    # Add CGM traces for each day
    for trace_info in aligned_traces:
        day_data = trace_info['data']
        
        fig.add_trace(go.Scatter(
            x=day_data['normalized_datetime'],
            y=day_data['sgv'],
            mode='lines',
            name=trace_info['name'],
            opacity=trace_info['opacity'],
            line=dict(width=trace_info['line_width']),
            showlegend=True,
            hovertemplate=f'<b>{trace_info["name"]}</b><br>%{{y}} mg/dL<br>%{{x|%H:%M}}<extra></extra>'
        ))
    
    # Add treatments if provided
    if treatments_by_day:
        for days_ago, treatments in treatments_by_day.items():
            if not treatments:
                continue
                
            opacity = 1.0 if days_ago == 0 else 0.5
            
            # Group treatments by type for this day
            treatment_types = {}
            for treatment in treatments:
                t_type = treatment['type']
                if t_type not in treatment_types:
                    treatment_types[t_type] = []
                treatment_types[t_type].append(treatment)
            
            # Add trace for each treatment type
            for treatment_type, type_treatments in treatment_types.items():
                x_values = [t['normalized_timestamp'] for t in type_treatments]
                y_values = [200 + (days_ago * 10)]  # Stack treatments vertically
                details = [t.get('details', '') for t in type_treatments]
                
                color = TREATMENT_COLORS.get(treatment_type, '#888888')
                
                fig.add_trace(go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode='markers',
                    name=f'{treatment_type} ({days_ago}d ago)' if days_ago > 0 else treatment_type,
                    marker=dict(
                        size=8 if days_ago == 0 else 6,
                        color=color,
                        opacity=opacity,
                        symbol='circle',
                        line=dict(width=1, color='white')
                    ),
                    customdata=details,
                    hovertemplate=f'<b>%{{fullData.name}}</b><br>%{{customdata}}<br>%{{x|%H:%M}}<extra></extra>',
                    showlegend=True
                ))
    
    # Add target range shading
    fig.add_hrect(y0=70, y1=180, 
                  fillcolor="rgba(76, 175, 80, 0.1)", 
                  line_width=0, 
                  annotation_text="Target Range")
    
    # Add reference lines
    fig.add_hline(y=70, line_dash="dash", line_color="red", opacity=0.5)
    fig.add_hline(y=180, line_dash="dash", line_color="orange", opacity=0.5)
    
    # Update layout for 24-hour x-axis
    fig.update_layout(
        title='Multi-Day CGM Pattern Overlay',
        xaxis=dict(
            title='Time of Day',
            tickformat='%H:%M',
            dtick=3600000,  # 1 hour intervals
        ),
        yaxis_title='Glucose (mg/dL)',
        height=700,
        hovermode='closest',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left", 
            x=0.01,
            font=dict(size=10)
        )
    )
    
    return fig
```

### Enhanced `app.py` for Stage 2

```python
import dash
from dash import dcc, html, Input, Output, callback, State
import plotly.graph_objects as go
from data.cgm_loader import get_cgm_data_custom
from data.treatment_loader import get_treatments_custom
from data.multi_day_loader import get_multi_day_aligned_data, create_aligned_traces, get_multi_day_treatments
from components.cgm_chart import create_cgm_chart
from components.multi_day_chart import create_multi_day_chart

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Multi-Day CGM Dashboard", style={'text-align': 'center'}),
    
    # Mode selection
    html.Div([
        html.Label("Chart Mode:"),
        dcc.RadioItems(
            id='chart-mode',
            options=[
                {'label': 'Single Period', 'value': 'single'},
                {'label': 'Multi-Day Overlay', 'value': 'multi'}
            ],
            value='single',
            inline=True,
            style={'margin-left': '10px'}
        )
    ], style={'padding': '10px', 'text-align': 'center'}),
    
    # Controls
    html.Div([
        html.Label("Time Range:"),
        dcc.Dropdown(
            id='time-range-dropdown',
            options=[
                {'label': 'Last 6 Hours', 'value': 6},
                {'label': 'Last 12 Hours', 'value': 12},
                {'label': 'Last 24 Hours', 'value': 24},
                {'label': 'Last 48 Hours', 'value': 48}
            ],
            value=24,
            style={'width': '200px', 'display': 'inline-block'}
        ),
        html.Label("Days to Overlay:", style={'margin-left': '20px'}),
        dcc.Dropdown(
            id='overlay-days',
            options=[
                {'label': '3 Days', 'value': 3},
                {'label': '7 Days', 'value': 7},
                {'label': '14 Days', 'value': 14}
            ],
            value=7,
            style={'width': '150px', 'display': 'inline-block', 'margin-left': '10px'}
        ),
        html.Button("Refresh Data", id="refresh-button", n_clicks=0,
                   style={'margin-left': '20px'})
    ], style={'padding': '20px', 'text-align': 'center'}),
    
    # Main chart
    dcc.Graph(id='cgm-chart', style={'height': '700px'}),
    
    # Summary stats
    html.Div(id='summary-stats', style={'padding': '20px'}),
    
    # Auto refresh every 5 minutes
    dcc.Interval(id='interval-component', interval=5*60*1000, n_intervals=0)
])

@callback(
    [Output('cgm-chart', 'figure'),
     Output('summary-stats', 'children')],
    [Input('chart-mode', 'value'),
     Input('time-range-dropdown', 'value'),
     Input('overlay-days', 'value'),
     Input('refresh-button', 'n_clicks'),
     Input('interval-component', 'n_intervals')]
)
def update_chart(chart_mode, hours, overlay_days, refresh_clicks, n_intervals):
    
    if chart_mode == 'single':
        # Single period mode
        cgm_df = get_cgm_data_custom(hours)
        treatments_df = get_treatments_custom(hours)
        fig = create_cgm_chart(cgm_df, treatments_df)
        
        # Summary for single period
        if not cgm_df.empty:
            avg_glucose = cgm_df['sgv'].mean()
            time_in_range = ((cgm_df['sgv'] >= 70) & (cgm_df['sgv'] <= 180)).sum() / len(cgm_df) * 100
            summary = html.Div([
                html.H4(f"Summary ({hours} hours)"),
                html.P(f"Average Glucose: {avg_glucose:.1f} mg/dL"),
                html.P(f"Time in Range: {time_in_range:.1f}%"),
                html.P(f"Readings: {len(cgm_df)}")
            ])
        else:
            summary = html.P("No data available")
    
    else:
        # Multi-day overlay mode
        multi_day_df = get_multi_day_aligned_data(overlay_days)
        aligned_traces = create_aligned_traces(multi_day_df)
        treatments_by_day = get_multi_day_treatments(overlay_days)
        fig = create_multi_day_chart(aligned_traces, treatments_by_day)
        
        # Summary for multi-day
        if not multi_day_df.empty:
            days_with_data = multi_day_df['days_ago'].nunique()
            total_readings = len(multi_day_df)
            avg_glucose = multi_day_df['sgv'].mean()
            summary = html.Div([
                html.H4(f"Multi-Day Summary ({overlay_days} days)"),
                html.P(f"Days with data: {days_with_data}"),
                html.P(f"Total readings: {total_readings}"),
                html.P(f"Overall average glucose: {avg_glucose:.1f} mg/dL")
            ])
        else:
            summary = html.P("No data available for overlay")
    
    return fig, summary

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
```

---

# Stage 3: Advanced Features

## Planned Enhancements

### Pattern Analysis Components

1. **Weekend vs Weekday Analysis**
2. **Meal Response Pattern Identification**  
3. **Exercise Impact Correlation**
4. **Sleep Pattern Analysis**

### Advanced Interactive Controls

1. **Custom Date Range Picker**
2. **Treatment Type Filtering**
3. **Pattern Overlay Toggles**
4. **Data Export Functionality**

### Analytics Dashboard

1. **Time in Range by Day Comparison**
2. **Treatment Effectiveness Scoring**
3. **Pattern Deviation Alerts**
4. **Predictive Trend Analysis**

---

# Implementation Notes

## Environment Setup

1. **Copy `.env` file** from your sweetiepy project to the new visualization project
2. **Use context managers** for all database connections (already implemented in sweetiepy)
3. **Handle timezone consistency** between CGM and treatment data

## Performance Considerations

1. **Limit data loading** to reasonable time ranges (max 30 days for multi-day)
2. **Cache data** when possible to avoid repeated database queries
3. **Use Plotly's built-in hover** and zoom features for interactivity
4. **Consider pagination** for very large datasets

## Data Quality Checks

1. **Validate timestamps** are in correct timezone
2. **Handle missing CGM data** gracefully  
3. **Filter out invalid glucose** values (< 20 or > 600)
4. **Align treatment timestamps** with CGM readings for overlay positioning

## Deployment Options

1. **Local development**: `python app.py`
2. **Docker container**: Create Dockerfile for containerized deployment
3. **Cloud deployment**: Use Heroku, AWS, or similar for public access
4. **Desktop app**: Consider using Electron wrapper for standalone app

## Extension Ideas

1. **Integration with other Loop data** (IOB, COB, predictions)
2. **Comparison with Nightscout** data for validation
3. **Machine learning** for pattern recognition and prediction
4. **Mobile-responsive design** for phone/tablet access
5. **Real-time data streaming** for live monitoring

---

# Getting Started

1. **Create the project structure** as outlined above
2. **Copy your `.env` file** from sweetiepy project
3. **Start with Stage 1** - basic 24-hour visualization
4. **Test with your data** to ensure proper connection and display
5. **Gradually add Stage 2** multi-day features
6. **Customize colors and styling** to your preferences

This plan provides a solid foundation for creating a comprehensive, interactive CGM visualization tool that leverages your existing sweetiepy infrastructure.