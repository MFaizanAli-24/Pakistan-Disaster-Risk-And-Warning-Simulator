from assessment_executors import perform_flood_risk_assessment, perform_drought_risk_assessment, perform_earthquake_risk_assessment
from storage import view_all_assessment_results

def main():
    menu = """
    1. Perform Flood Risk Assessment
    2. Perform Drought Risk Assessment
    3. Perform Earthquake Risk Assessment
    4. View All Assessment Results
    5. Exit
    """

    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            perform_flood_risk_assessment()
        elif choice == "2":
            perform_drought_risk_assessment()
        elif choice == "3":
            perform_earthquake_risk_assessment()
        elif choice == "4":
            view_all_assessment_results()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()