# medical_history_data.py
CLINICAL_CASES = [
    # Format: [Symptom Description, Category]
    ["Patient reports sharp pressure in chest, radiating to jaw. Sweating heavily.", "URGENT"],
    ["Child swallowed a small coin and is gasping for air.", "URGENT"],
    ["Sudden onset of slurred speech and right-sided facial droop.", "URGENT"],
    ["Severe allergic reaction: throat closing, hives appearing after nut consumption.", "URGENT"],
    ["Compound fracture: bone visible through skin after a fall.", "URGENT"],
    ["Mild nasal congestion, clear discharge, no fever for 2 days.", "SIMPLE"],
    ["Small red rash on forearm, slightly itchy, no spreading.", "SIMPLE"],
    ["Twisted ankle while running, slight swelling, can still bear weight.", "SIMPLE"],
    ["Minor sunburn on shoulders after beach trip, skin is pink but not blistering.", "SIMPLE"],
    ["Lower back stiffness after sitting at a desk for 8 hours.", "SIMPLE"],
    # In a real project, you would have 1000+ of these from a CSV file.
]