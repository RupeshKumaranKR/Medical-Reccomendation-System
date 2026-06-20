import ollama
import pandas as pd
import medical_logic # Our anatomy map

def advanced_diagnostic():
    print("\n--- MEDICAL ASSISTANT: ANATOMICAL SEARCH ---")
    user_input = input("Where do you feel the pain and what are the symptoms? ").lower()

    # 1. Identify the Body Part
    target_part = "GENERAL"
    for keyword, part in medical_logic.SYMPTOM_TO_BODY_PART.items():
        if keyword in user_input:
            target_part = part
            break
    
    print(f"📍 Target Anatomy: {target_part}")

    # 2. Check if the symptoms relate to your 55k CSV Data
    # List of conditions we actually have in the CSV:
    csv_conditions = ["Arthritis", "Diabetes", "Hypertension", "Obesity", "Cancer", "Asthma"]
    
    match_found = any(cond.lower() in user_input for cond in csv_conditions)

    if match_found:
        print("📊 Data Match: Analyzing patterns from Healthcare Dataset...")
        # Use your ML Triage from earlier here
    else:
        print("💡 Special Case: Symptom not in CSV. Engaging Meditron Knowledge Base...")

    # 3. Use LLM to give specific Body-Part Advice
    prompt = f"""
    The user is complaining of symptoms in the {target_part} area.
    Symptom Description: {user_input}
    
    If this is a potential FRACTURE, give immediate First Aid for bones.
    If this is a simple FEVER/COLD, give home remedies.
    Provide 3 steps and 1 major precaution.
    """
    
    response = ollama.generate(model='meditron', prompt=prompt)
    print("\n--- CLINICAL RECOMMENDATION ---")
    print(response['response'])

if __name__ == "__main__":
    advanced_diagnostic()