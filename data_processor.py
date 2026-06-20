import pandas as pd

def download_and_clean_data():
    print("Fetching clinical dataset from GitHub/Kaggle source...")
    # This is a cleaned version of the Symptom2Disease dataset
    url = "https://raw.githubusercontent.com/Anujit-Ghosh/Symptom2Disease/main/Symptom2Disease.csv"
    
    try:
        df = pd.read_csv(url)
    except:
        print("Error: Could not download. Make sure you have an internet connection.")
        return None

    # We need to map real medical labels to our Triage System
    # Urgent = Life threatening or contagious
    # Simple = Chronic, manageable, or minor
    urgency_map = {
        'Psoriasis': 'SIMPLE',
        'Varicose Veins': 'SIMPLE',
        'Typhoid': 'URGENT',
        'Chicken pox': 'URGENT',
        'Impetigo': 'SIMPLE',
        'Dengue': 'URGENT',
        'Fungal infection': 'SIMPLE',
        'Common Cold': 'SIMPLE',
        'Pneumonia': 'URGENT',
        'Dimorphic Hemorrhoids': 'SIMPLE',
        'Arthritis': 'SIMPLE',
        'Acne': 'SIMPLE',
        'Bronchial Asthma': 'URGENT',
        'Hypertension': 'URGENT',
        'Migraine': 'SIMPLE',
        'Cervical spondylosis': 'SIMPLE',
        'Jaundice': 'URGENT',
        'Malaria': 'URGENT',
        'Urinary tract infection': 'SIMPLE',
        'Allergy': 'SIMPLE',
        'Gastroesophageal reflux disease': 'SIMPLE',
        'Drug Reaction': 'URGENT',
        'Peptic ulcer disease': 'SIMPLE',
        'Diabetes': 'SIMPLE'
    }

    # Apply the mapping
    df['triage'] = df['label'].map(urgency_map)
    
    # Save it to your Z drive project folder
    df.to_csv("clinical_cases_full.csv", index=False)
    print(f"✅ Success! 1200+ Clinical cases saved to 'clinical_cases_full.csv'")
    return df

if __name__ == "__main__":
    download_and_clean_data()