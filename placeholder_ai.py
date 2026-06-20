import time

def analyze_symptoms_placeholder(user_input):
    print("\n[AI System] Analyzing symptoms locally...")
    time.sleep(1.5)  # Simulates processing time for the demo

    # 1. Define "Red Flag" Keywords for Urgency
    urgent_keywords = [
        "chest pain", "breathing", "heavy bleeding", "unconscious", 
        "vision loss", "severe abdominal pain", "stroke", "seizure"
    ]
    
    # 2. Define "Simple" Keywords
    simple_keywords = [
        "cold", "cough", "sore throat", "fever", "itch", "rash", "headache"
    ]

    # Convert input to lowercase for better matching
    user_input = user_input.lower()
    
    # 3. Simple Logic-based Analysis (The "AI" part)
    urgency_score = 0
    for word in urgent_keywords:
        if word in user_input:
            urgency_score += 10
            
    # 4. Final Categorization
    if urgency_score >= 10:
        return {
            "status": "URGENT",
            "confidence": "High",
            "advice": "FIRST AID: Stay calm. Call 911 or visit the ER immediately. Do not drive yourself.",
            "reasoning": "Detected critical symptoms indicating potential cardiovascular or respiratory distress."
        }
    else:
        return {
            "status": "SIMPLE",
            "confidence": "Moderate",
            "advice": "HOME CARE: Rest, stay hydrated, and monitor symptoms. Consult a GP if it persists.",
            "reasoning": "Symptoms appear non-life-threatening. Matches standard viral/mild bacterial profiles."
        }

# --- Demo Interface ---
print("--- MEDICAL RECOMMENDATION SYSTEM (v0.1 Prototype) ---")
user_input = input("Please describe your symptoms: ")
result = analyze_symptoms_placeholder(user_input)

print("-" * 50)
print(f"DIAGNOSIS CATEGORY: {result['status']}")
print(f"ANALYSIS CONFIDENCE: {result['confidence']}")
print(f"AI REASONING: {result['reasoning']}")
print(f"ACTION PLAN: {result['advice']}")
print("-" * 50)