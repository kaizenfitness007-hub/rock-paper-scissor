def calculate_e1rm():
    print("--- Iron Logic: Fatigue & 1RM Tracker ---")
    
    weight = float(input("Weight lifted (lbs): "))
    rpe = float(input("RPE (1-10): "))
    
    # The Math: Adjusting for RPE
    e1rm = weight / (1 - (0.025 * (10 - rpe)))
    
    print(f"\nYour Estimated 1RM for this lift is: {round(e1rm, 2)} lbs")
    
    # Fatigue Logic
    if rpe >= 9.5:
        print("⚠️ ALERT: CNS Fatigue is high. Recommend deloading accessory volume by 10%.")
    else:
        print("✅ Recovery looks good. Stay on the current program.")

calculate_e1rm()
import csv
import os
from datetime import datetime

def log_lift():
    print("--- Iron Ledger: Log Your Lift ---")
    
    # User Input
    exercise = input("Exercise name (e.g., Deadlift): ")
    weight = float(input("Weight (lbs): "))
    rpe = float(input("RPE (1-10): "))
    
    # Calculation
    e1rm = weight / (1 - (0.025 * (10 - rpe)))
    
    # Save to file
    file_exists = os.path.isfile('training_log.csv')
    
    with open('training_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # Write header if file is new
        if not file_exists:
            writer.writerow(['Date', 'Exercise', 'Weight', 'RPE', 'Estimated_1RM'])
        
        # Write the data
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), exercise, weight, rpe, round(e1rm, 2)])
        
    print(f"\n✅ Logged: {exercise} | E1RM: {round(e1rm, 2)} lbs")

log_lift()