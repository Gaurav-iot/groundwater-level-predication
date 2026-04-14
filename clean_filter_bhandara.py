# ✅ Clean both CSV files
# ✅ Normalize district and date columns
# ✅ Filter for Bhandara district in Maharashtra
# ✅ Merge both datasets
# ✅ Save the filtered and merged data to a CSV

import pandas as pd

# STEP 1: Load the datasets
rainfall_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\daily-rainfall-data-district-level.csv"
telemetry_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\cgwb-changes-in-depth-to-water-level.csv"

# Read with correct encoding
df_rainfall = pd.read_csv(rainfall_path, encoding='ISO-8859-1')
df_telemetry = pd.read_csv(telemetry_path, encoding='ISO-8859-1')

# STEP 2: Normalize column names for merging
df_rainfall.rename(columns={'district_name': 'District'}, inplace=True)
df_telemetry.rename(columns={'district_name': 'District'}, inplace=True)

# Convert to lowercase + strip spaces for consistent matching
df_rainfall['District'] = df_rainfall['District'].str.lower().str.strip()
df_telemetry['District'] = df_telemetry['District'].str.lower().str.strip()

df_rainfall['state_name'] = df_rainfall['state_name'].str.lower().str.strip()
df_telemetry['state_name'] = df_telemetry['state_name'].str.lower().str.strip()

# STEP 3: Convert date to datetime
df_rainfall['date'] = pd.to_datetime(df_rainfall['date'], errors='coerce')
df_telemetry['date'] = pd.to_datetime(df_telemetry['date'], errors='coerce')

# STEP 4: Filter Maharashtra & Bhandara
df_rainfall = df_rainfall[(df_rainfall['state_name'] == 'maharashtra') & (df_rainfall['District'] == 'bhandara')]
df_telemetry = df_telemetry[(df_telemetry['state_name'] == 'maharashtra') & (df_telemetry['District'] == 'bhandara')]

# STEP 5: Merge both on date and District
merged_df = pd.merge(df_telemetry, df_rainfall, on=['date', 'District'], how='inner')

# STEP 6: Save the merged data
output_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\bhandara_merged.csv"
merged_df.to_csv(output_path, index=False)

print("✅ Success! Filtered and merged data saved to:")
print(output_path)


