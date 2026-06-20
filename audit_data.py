import pandas as pd

# Load the file
df = pd.read_csv("healthcare_dataset.csv")

# 1. Check total size
rows, columns = df.shape
print(f"📊 TOTAL RECORDS FOUND: {rows}")
print(f"📊 TOTAL COLUMNS FOUND: {columns}")

# 2. See how many of each 'Medical Condition' you have
print("\n🔍 CASES PER CONDITION:")
print(df['Medical Condition'].value_counts())

# 3. See how many of each 'Admission Type' you have
print("\n🚑 ADMISSION TYPES (Triage Data):")
print(df['Admission Type'].value_counts())