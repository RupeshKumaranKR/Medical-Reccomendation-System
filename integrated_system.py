import ollama
import pandas as pd
import pickle
import time

# Load Data
df = pd.read_csv("healthcare_dataset.csv")
with open('triage_model.pkl', 'rb') as f: ml_model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f: vectorizer = pickle.load(f)

def run_system():
    print("\n" + "="*60)
    print("      DATA-DRIVEN MEDICAL RECOMMENDATION SYSTEM")
    print("="*60)
    
    user_input = input("\nDescribe how you feel (e.g., 'I have sharp chest pain'): ")

    # PHASE 1: LLM INTERPRETATION (Mapping symptoms to CSV Conditions)
    # We ask the LLM to pick a category that exists in your healthcare_dataset.csv
    conditions_list = df['Medical Condition'].unique().tolist()
    
    interpret_prompt = f"""
    The user says: '{user_input}'
    Pick the most likely Medical Condition from this list: {conditions_list}.
    Return ONLY the name of the condition.
    """
    
    print("[AI] Interpreting symptoms...")
    predicted_condition = ollama.generate(model='meditron', prompt=interpret_prompt)['response'].strip()

    # PHASE 2: ML TRIAGE (Checking urgency from the CSV pattern)
    vec_input = vectorizer.transform([predicted_condition])
    triage_result = ml_model.predict(vec_input)[0]

    # PHASE 3: RECOMMENDATION
    if triage_result == "URGENT":
        print(f"\n🚨 ALERT: THIS IS A POTENTIAL '{predicted_condition.upper()}' CASE.")
        print("TRIAGE STATUS: URGENT / EMERGENCY (Based on Clinical Dataset)")
        print("\nACTION PLAN:")
        print("1. CALL EMERGENCY SERVICES IMMEDIATELY.")
        print("2. FIRST AID: Rest, do not ingest anything, wait for professionals.")
    else:
        print(f"\n✅ CONDITION IDENTIFIED: {predicted_condition}")
        print("TRIAGE STATUS: SIMPLE / ELECTIVE")
        
        # Get cure from CSV + LLM
        # Look up typical medication in your CSV for this condition
        sample_med = df[df['Medical Condition'] == predicted_condition]['Medication'].iloc[0]
        
        print(f"\n[AI Recommendation based on Local Healthcare Data]:")
        
        advice_prompt = f"""
        Provide 3 simple home remedies and 2 precautions for a patient feeling '{user_input}' 
        associated with '{predicted_condition}'. 
        (Historical medication for this in our database includes: {sample_med}).
        Keep advice simple and safe.
        """
        
        advice = ollama.generate(model='meditron', prompt=advice_prompt)['response']
        print(advice)

if __name__ == "__main__":
    while True:
        run_system()
        if input("\nAnalyze another patient? (y/n): ").lower() == 'n': break