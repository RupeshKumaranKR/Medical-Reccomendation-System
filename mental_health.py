import pandas as pd

# This bridges the gap between lifestyle (Stress) and symptoms (Panic)
mental_health_data = [
    {"Medical Condition": "Panic Attack", "Symptoms": "shortness of breath, racing heart, heightened anxiety, feeling of impending doom, nausea, shivering", "Medication": "Breathing techniques, Therapy", "Admission Type": "Elective"},
    {"Medical Condition": "Generalized Anxiety", "Symptoms": "constant worrying, restless, fatigue, muscle tension, sweating", "Medication": "CBT, Mindfulness", "Admission Type": "Elective"},
    {"Medical Condition": "Insomnia", "Symptoms": "difficulty falling asleep, staying awake at night, tired during day, irritability", "Medication": "Sleep hygiene, Melatonin", "Admission Type": "Elective"},
    {"Medical Condition": "Depression", "Symptoms": "persistent sadness, loss of interest, change in appetite, sleeping too much or too little", "Medication": "Counseling, Support groups", "Admission Type": "Elective"}
]

# We expand this to 500 rows so it has weight in your system
df_mental = pd.DataFrame(mental_health_data * 125)
df_mental.to_csv("Anatomy_Data/Mental_Health.csv", index=False)
print("✅ Mental_Health.csv created with symptom-to-lifestyle mappings!")