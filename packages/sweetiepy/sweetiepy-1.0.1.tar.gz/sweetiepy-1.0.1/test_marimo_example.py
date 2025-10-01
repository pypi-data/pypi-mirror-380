#!/usr/bin/env python
"""
Simple test script for verifying SweetiePy works in Marimo notebooks.
Copy and paste these code blocks into separate Marimo cells.
"""

# Cell 1: Basic imports and connection test
def test_connection():
    from sweetiepy.data.cgm import CGMDataAccess
    
    print("🔍 Testing connection...")
    with CGMDataAccess() as cgm:
        cgm.get_collection_info()
    print("✅ Connection successful!")

# Cell 2: Basic CGM analysis (safe approach)
def basic_cgm_analysis():
    from sweetiepy.data.cgm import CGMDataAccess
    
    with CGMDataAccess() as cgm:
        df = cgm.get_dataframe_for_period('last_week')
        
        print(f"📊 {len(df)} glucose readings analyzed")
        print(f"📅 Date range: {df['datetime'].min()} to {df['datetime'].max()}")
        print(f"🩸 Average glucose: {df['sgv'].mean():.1f} mg/dL")
        
        # Manual time in range calculation (always works)
        total_readings = len(df)
        in_range = ((df['sgv'] >= 70) & (df['sgv'] <= 180)).sum()
        high = (df['sgv'] > 180).sum()
        low = (df['sgv'] < 70).sum()
        
        print(f"🎯 Time in range (70-180): {in_range/total_readings*100:.1f}%")
        print(f"📈 Time high (>180): {high/total_readings*100:.1f}%")
        print(f"📉 Time low (<70): {low/total_readings*100:.1f}%")

# Cell 3: Using the analyze_dataframe method
def advanced_cgm_analysis():
    from sweetiepy.data.cgm import CGMDataAccess
    
    with CGMDataAccess() as cgm:
        df = cgm.get_dataframe_for_period('last_week')
        analysis = cgm.analyze_dataframe(df)
        
        # Check if analysis was successful
        if 'error' in analysis:
            print(f"❌ Analysis error: {analysis['error']}")
            return
            
        print(f"📊 {analysis['basic_stats']['total_readings']} glucose readings analyzed")
        print(f"🩸 Average glucose: {analysis['basic_stats']['avg_glucose']:.1f} mg/dL")
        print(f"🎯 Time in range: {analysis['time_in_range']['normal_percent']:.1f}%")
        print(f"📈 Time high: {analysis['time_in_range']['high_percent']:.1f}%")
        print(f"📉 Time low: {analysis['time_in_range']['low_percent']:.1f}%")
        
        return analysis

# Cell 4: Data exploration
def explore_data():
    from sweetiepy.data.cgm import CGMDataAccess
    
    with CGMDataAccess() as cgm:
        df = cgm.get_dataframe_for_period('last_week')
        
        print("🔍 Data Overview:")
        print(f"  Shape: {df.shape}")
        print(f"  Columns: {list(df.columns)}")
        print(f"  Glucose range: {df['sgv'].min()}-{df['sgv'].max()} mg/dL")
        
        # Show data types
        print("\n📋 Column types:")
        for col in df.columns:
            print(f"  {col}: {df[col].dtype}")
        
        # Show sample data
        print("\n📊 Sample data:")
        print(df[['datetime', 'sgv', 'direction', 'glucose_category']].head())
        
        return df

if __name__ == "__main__":
    print("🧪 Running all tests...")
    
    # Test connection
    test_connection()
    
    # Basic analysis
    print("\n" + "="*50)
    basic_cgm_analysis()
    
    # Advanced analysis
    print("\n" + "="*50)
    analysis = advanced_cgm_analysis()
    
    # Data exploration
    print("\n" + "="*50)
    df = explore_data()
    
    print("\n✅ All tests completed!")