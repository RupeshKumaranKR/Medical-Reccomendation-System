import pandas as pd
import os

df = pd.read_csv("healthcare_dataset.csv")

# Create a folder for the dataset split
if not os.path.exists("Anatomy_Data"):
    os.makedirs("Anatomy_Data")

# Group 1: Chest (Asthma, Hypertension)
chest_df = df[df['Medical Condition'].isin(['Asthma', 'Hypertension'])]
chest_df.to_csv("Anatomy_Data/Chest_Heart.csv", index=False)

# Group 2: Abdomen (Diabetes, Obesity)
abdomen_df = df[df['Medical Condition'].isin(['Diabetes', 'Obesity'])]
abdomen_df.to_csv("Anatomy_Data/Abdomen.csv", index=False)

# Group 3: Limbs (Arthritis)
limbs_df = df[df['Medical Condition'] == 'Arthritis']
limbs_df.to_csv("Anatomy_Data/Limbs_Bones.csv", index=False)

# Group 4: Complex (Cancer)
complex_df = df[df['Medical Condition'] == 'Cancer']
complex_df.to_csv("Anatomy_Data/Systemic_Complex.csv", index=False)

print("📁 Datasets split by Anatomy! Check the 'Anatomy_Data' folder.")