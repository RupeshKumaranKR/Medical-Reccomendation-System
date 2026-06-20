# medical_logic.py

# Categorizing by Body Part
ANATOMY_MAP = {
    "HEAD/BRAIN": {
        "conditions": ["Migraine", "Stroke", "Concussion", "Brain Tumor", "Meningitis"],
        "simple_ailments": ["Headache", "Dizziness", "Brain Fog"],
        "urgency": "HIGH"
    },
    "CHEST/HEART": {
        "conditions": ["Hypertension", "Asthma", "Heart Attack", "Pneumonia"],
        "simple_ailments": ["Cough", "Shortness of breath", "Palpitations"],
        "urgency": "CRITICAL"
    },
    "ABDOMEN/DIGESTION": {
        "conditions": ["Diabetes", "Obesity", "Appendicitis", "Food Poisoning"],
        "simple_ailments": ["Stomach Ache", "Bloating", "Acidity"],
        "urgency": "MEDIUM"
    },
    "LIMBS/BONES": {
        "conditions": ["Arthritis", "Fracture", "Sprain", "Gout"],
        "simple_ailments": ["Joint Stiffness", "Muscle Cramp", "Swelling"],
        "urgency": "LOW/MEDIUM"
    }
}

# Mapping common symptoms to these parts for the "Initial Triage"
SYMPTOM_TO_BODY_PART = {
    "vision": "HEAD/BRAIN", "slurred": "HEAD/BRAIN", "head": "HEAD/BRAIN",
    "chest": "CHEST/HEART", "breath": "CHEST/HEART", "heart": "CHEST/HEART",
    "stomach": "ABDOMEN/DIGESTION", "belly": "ABDOMEN/DIGESTION", "nausea": "ABDOMEN/DIGESTION",
    "leg": "LIMBS/BONES", "arm": "LIMBS/BONES", "bone": "LIMBS/BONES", "joint": "LIMBS/BONES",
    "anxiety": "Mental_Health.csv",
    "panic": "Mental_Health.csv",
    "nervous": "Mental_Health.csv",
    "scared": "Mental_Health.csv",
    "shivering": "Mental_Health.csv", # Shivering is a key panic symptom
    "night": "Mental_Health.csv"      # Traumatic memories often happen at night
}