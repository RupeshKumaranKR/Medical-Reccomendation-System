# triage_engine.py
import pickle
import medical_data

# Load the ML "Brain"
with open('triage_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def evaluate_urgency(user_text):
    # ML Prediction
    input_vector = vectorizer.transform([user_text.lower()])
    prediction = model.predict(input_vector)[0]
    
    # Check probabilities (how sure is the AI?)
    probs = model.predict_proba(input_vector)[0]
    confidence = max(probs)

    # Logic: If ML is very confident, use its result. 
    # Otherwise, fallback to a safety check.
    if confidence > 0.4:
        return prediction, f"ML Analysis (Confidence: {confidence:.2f})"
    
    return "UNKNOWN", "Insufficient data for ML analysis"

def get_treatment_plan(category, detail):
    # (Keep the same logic as the previous version)
    if category == "URGENT":
        return {
            "action": "IMMEDIATE MEDICAL ATTENTION",
            "steps": ["Call emergency services", "Stay seated/lying down"],
            "warning": "ML detected high-risk patterns."
        }
    else:
        return {
            "action": "Standard Care Protocol",
            "steps": ["Rest", "Monitor symptoms", "Hydrate"],
            "warning": "Seek a doctor if symptoms worsen."
        }