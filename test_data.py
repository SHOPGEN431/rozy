import pandas as pd
from collections import defaultdict

def load_llc_data():
    csv_path = r"C:\rozy\LLC Data.csv"
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()

def test_data_loading():
    print("Testing CSV data loading...")
    df = load_llc_data()
    
    if df.empty:
        print("❌ Failed to load CSV data")
        return
    
    print(f"✅ Successfully loaded CSV with {len(df)} records")
    print(f"📊 Columns: {list(df.columns)}")
    
    # Check state data
    states = df['state'].dropna().unique()
    print(f"🗺️  Found {len(states)} unique states:")
    for state in sorted(states)[:10]:  # Show first 10 states
        count = len(df[df['state'] == state])
        print(f"   - {state}: {count} services")
    
    # Check sample data
    print("\n📋 Sample records:")
    sample = df.head(3)
    for _, row in sample.iterrows():
        print(f"   - {row.get('name', 'N/A')} in {row.get('city', 'N/A')}, {row.get('state', 'N/A')}")
    
    # Test state filtering
    print("\n🔍 Testing state filtering...")
    florida_data = df[df['state'].str.contains('Florida', case=False, na=False)]
    print(f"   Florida services: {len(florida_data)}")
    
    california_data = df[df['state'].str.contains('California', case=False, na=False)]
    print(f"   California services: {len(california_data)}")

if __name__ == "__main__":
    test_data_loading()
