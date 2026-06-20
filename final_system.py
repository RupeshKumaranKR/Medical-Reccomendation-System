import ollama
import pandas as pd
import os
import pickle

# --- SETUP & IMPORTS ---
DATA_DIR = "Anatomy_Data"

print("1. Loading incremental training models...")
with open('triage_model.pkl', 'rb') as f: ml_model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f: vectorizer = pickle.load(f)

# Anatomical Routing Map
ROUTING_MAP = {
    "chest": "Chest_Heart.csv", "breath": "Chest_Heart.csv", "heart": "Chest_Heart.csv",
    "stomach": "Abdomen.csv", "belly": "Abdomen.csv", "diabetes": "Abdomen.csv",
    "leg": "Limbs_Bones.csv", "arm": "Limbs_Bones.csv", "bone": "Limbs_Bones.csv", "joint": "Limbs_Bones.csv",
    "head": "General", "shiver": "General", "fever": "General", "dizzy": "General",
    "abdomen": "Abdomen.csv",
    "side": "Abdomen.csv",
    "gallbladder": "Abdomen.csv",
    "anxiety": "Mental_Health.csv",
    "panic": "Mental_Health.csv",
    "shiver": "Mental_Health.csv"
}

def run_diagnostic():
    print("\n" + "█"*60)
    print("      MEDICAL RECOMMENDATION SYSTEM (v3.0 FINAL)")
    print("█"*60)

    # STEP 1: USER INPUT (Must be at the top!)
    user_input = input("\n[USER] Describe your symptoms: ").lower()
    
    # Define priorities: Internal Organs > Limbs
    priority_order = ["chest", "stomach", "abdomen", "belly", "head", "brain", "leg", "arm", "joint"]
    
    target_csv = "General"
    for part in priority_order:
        if part in user_input:
            # Match the part to the CSV filename
            for key, value in ROUTING_MAP.items():
                if key == part:
                    target_csv = value
                    break
            if target_csv != "General": break # Found the high-priority match

    print(f"📍 Analysis Focus: {target_csv}")

    # STEP 2: ANATOMICAL DATA SEARCH
    target_csv = "General"
    historical_context = ""
    for key, value in ROUTING_MAP.items():
        if key in user_input:
            target_csv = value
            break

    if target_csv != "General":
        csv_path = os.path.join(DATA_DIR, target_csv)
        if os.path.exists(csv_path):
            df_slice = pd.read_csv(csv_path).head(50)
            avg_age = int(df_slice['Age'].mean())
            common_med = df_slice['Medication'].mode()[0]
            historical_context = f"Context: Database shows average patient age of {avg_age} for this area, commonly treated with {common_med}."
            print(f"📊 [DATABASE] Routed to {target_csv}")
    else:
        print("💡 [LLM] Using General Clinical Knowledge.")

    # STEP 3: ML TRIAGE CHECK (The 55k row Brain)
    vec_input = vectorizer.transform([user_input])
    triage_status = ml_model.predict(vec_input)[0]

    # STEP 4: LLAMA 3 CHAT RECOMMENDATION
    messages = [
        {
            'role': 'system', 
            'content': """You are a highly accurate Medical Diagnostic Assistant.
            
            CRITICAL KNOWLEDGE:
            1. REFERRED PAIN: Pain in the RIGHT shoulder/arm + RIGHT abdomen usually indicates Gallbladder (Cholecystitis) or Liver issues.
            2. CARDIAC PAIN: Pain in the LEFT shoulder/arm + CHEST indicates Heart (Angina/MI).
            
            Do not confuse Right-sided pain with Heart Attacks.
            
            Provide:
            1. STATUS: (Urgent/Simple)
            2. ANALYSIS: (Mention if it's Referred Pain from an organ)
            3. CAUSE: (Identify the likely organ)
            4. REMEDIES: (Immediate actions)
            5. PRECAUTION: (One major warning)"""
        },
        {
            'role': 'user', 
            'content': f"Triage: {triage_status}\nContext: {historical_context}\nPatient Symptoms: {user_input}"
        }
    ]

    print("\n" + "🩺 " + "-"*20 + " CLINICAL REPORT " + "-"*20)
    
    try:
        stream = ollama.chat(model='llama3', messages=messages, stream=True)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
    
    print("\n" + "-" * 57)

if __name__ == "__main__":
    while True:
        run_diagnostic()
        if input("\nNew diagnostic? (y/n): ").lower() == 'n': break