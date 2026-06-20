import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import HashingVectorizer
import pickle
import time

def train_in_parts():
    print("🚀 INITIALIZING INCREMENTAL TRAINING SYSTEM...")
    
    # 1. Load both datasets
    df_physical = pd.read_csv("healthcare_dataset.csv")
    df_mental = pd.read_csv("Mental_Health.csv")
    
    # COMBINE THEM into one big dataframe
    df = pd.concat([df_physical, df_mental], ignore_index=True)
    
    # Safety: Remove spaces from columns
    df.columns = df.columns.str.strip() 

    # Prep the target data (Now it will have both URGENT and SIMPLE)
    df['triage'] = df['Admission Type'].apply(lambda x: 'URGENT' if x in ['Emergency', 'Urgent'] else 'SIMPLE')
    
    vectorizer = HashingVectorizer(stop_words='english', n_features=2**15)
    model = SGDClassifier(loss='log_loss') 
    
    # Ensure classes are exactly ['SIMPLE', 'URGENT']
    classes = np.array(['SIMPLE', 'URGENT'])

    # 2. Split data into 5 Parts using PURE PANDAS logic
    num_parts = 5
    chunk_size = len(df) // num_parts

    for i in range(num_parts):
        part_num = i + 1
        print(f"\n--- 🧩 PART {part_num} OF {num_parts} ---")
        
        # We use .iloc to slice the DataFrame safely (keeps headers intact!)
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i != num_parts - 1 else len(df)
        
        current_batch = df.iloc[start_idx:end_idx]
        print(f"Feeding {len(current_batch)} records into the brain...")
        
        # TRAINING
        X_batch = vectorizer.transform(current_batch['Medical Condition'].astype(str))
        y_batch = current_batch['triage']
        
        start_time = time.time()
        model.partial_fit(X_batch, y_batch, classes=classes)
        
        print(f"✅ Part {part_num} complete! (Time: {round(time.time()-start_time, 4)}s)")
        
        if part_num < num_parts:
            if input(f"Proceed to Part {part_num + 1}? (y/n): ").lower() != 'y':
                print("🛑 Pausing...")
                break

    # 3. Final Save
    print("\n💾 Saving optimized models to Z: Drive...")
    with open('triage_model.pkl', 'wb') as f: pickle.dump(model, f)
    with open('vectorizer.pkl', 'wb') as f: pickle.dump(vectorizer, f)
    print("🎊 ALL DATA PROCESSED SUCCESSFULLY.")

if __name__ == "__main__":
    train_in_parts()