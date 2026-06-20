# medical_data.py

# Red flags that trigger an URGENT status
EMERGENCY_SYMPTOMS = {
    "cardiac": ["chest pain", "left arm pain", "heart racing", "palpitations"],
    "respiratory": ["shortness of breath", "difficulty breathing", "wheezing"],
    "neurological": ["slurred speech", "numbness", "severe dizziness", "fainting"],
    "trauma": ["heavy bleeding", "deep cut", "broken bone"]
}

# Simple ailments and their recommended care
SIMPLE_AILMENTS = {
    "common cold": {
        "symptoms": ["sneezing", "runny nose", "mild cough"],
        "remedies": ["Hydration", "Rest", "Vitamin C", "Steam inhalation"],
        "precaution": "Monitor fever; if it exceeds 102°F, see a doctor."
    },
    "migraine": {
        "symptoms": ["headache", "sensitivity to light", "nausea"],
        "remedies": ["Dark room rest", "Hydration", "Magnesium supplements"],
        "precaution": "Seek help if this is the 'worst headache of your life'."
    },
    "indigestion": {
        "symptoms": ["stomach ache", "bloating", "heartburn"],
        "remedies": ["Ginger tea", "Avoid spicy food", "Small meals"],
        "precaution": "If pain moves to lower right abdomen, seek urgent care (Appendicitis risk)."
    }
}