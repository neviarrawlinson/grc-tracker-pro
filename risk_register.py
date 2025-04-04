import csv
import os

# File to store the risk data
file_name = "risks.csv"

# Function to add a risk entry
def add_risk():
    risk_name = input("Enter the risk name: ")
    likelihood = int(input("Enter likelihood (1-5): "))
    impact = int(input("Enter impact (1-5): "))
    
    risk_score = likelihood * impact
    print(f"\nRisk '{risk_name}' has a score of {risk_score}.\n")

    file_exists = os.path.isfile(file_name)

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Risk Name", "Likelihood", "Impact", "Risk Score"])
        writer.writerow([risk_name, likelihood, impact, risk_score])

    print("Risk saved to risks.csv ✅")

# Function to view saved risks
def view_risks():
    if not os.path.exists(file_name):
        print("No risks found. Add some first.")
        return

    print("\n📋 Risk Register:\n")
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()

# Main menu
if __name__ == "__main__":
    print("Welcome to GRC Tracker Pro")
    print("1. Add a new risk")
    print("2. View saved risks")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        add_risk()
    elif choice == "2":
        view_risks()
    else:
        print("Invalid choice.")
