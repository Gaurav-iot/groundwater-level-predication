import pandas as pd

# STEP 1: Load the datasets (correct path with quotes and raw string to avoid backslash errors)
rainfall_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\daily-rainfall-data-district-level.csv"
telemetry_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\cgwb-changes-in-depth-to-water-level.csv"

df_rainfall = pd.read_csv(rainfall_path)
df_telemetry = pd.read_csv(telemetry_path)

# STEP 2: Show columns for debugging
print("✅ Rainfall dataset columns:", df_rainfall.columns.tolist())
print("✅ Telemetry dataset columns:", df_telemetry.columns.tolist())

# STEP 3: Rename and clean columns if needed
df_rainfall.rename(columns={'district_name': 'District'}, inplace=True)
df_telemetry.rename(columns={'district_name': 'District'}, inplace=True)

# Rename date column in telemetry to 'date' if needed
if 'observation_date' in df_telemetry.columns:
    df_telemetry.rename(columns={'observation_date': 'date'}, inplace=True)
elif 'date' not in df_telemetry.columns:
    raise KeyError("❌ No valid date column found in telemetry dataset!")

# STEP 4: Convert date columns to datetime format
df_rainfall['date'] = pd.to_datetime(df_rainfall['date'], errors='coerce')
df_telemetry['date'] = pd.to_datetime(df_telemetry['date'], errors='coerce')

# STEP 5: Normalize district names to lowercase for consistency
df_rainfall['District'] = df_rainfall['District'].str.lower().str.strip()
df_telemetry['District'] = df_telemetry['District'].str.lower().str.strip()

# STEP 6: Round telemetry dates to the nearest day (remove time component)
df_telemetry['date'] = df_telemetry['date'].dt.floor('D')

# STEP 7: Merge on date + district (inner join keeps only matched rows)
merged_df = pd.merge(df_telemetry, df_rainfall, on=['date', 'District'], how='inner')

# STEP 8: Save and preview result
print("✅ Merged Data Preview:")
print(merged_df.head())

output_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\merged_groundwater_maharashtra.csv"
merged_df.to_csv(output_path, index=False)
print(f"📁 File saved at: {output_path}")




# to know the columns names in order to clean the datasets

import pandas as pd

rainfall_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\daily-rainfall-data-district-level.csv"
telemetry_path = r"C:\Users\Vanshri Madam\PycharmProjects\SmartGroundwaterPrediction\data\cgwb-changes-in-depth-to-water-level.csv"

df_rainfall = pd.read_csv(rainfall_path, encoding='ISO-8859-1')
df_telemetry = pd.read_csv(telemetry_path, encoding='ISO-8859-1')

print("Rainfall Columns:\n", df_rainfall.columns.tolist())
print("\nTelemetry Columns:\n", df_telemetry.columns.tolist())
