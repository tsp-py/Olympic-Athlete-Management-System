from data import olympic_list
from athlete_manager import AthleteManager

if __name__ == "__main__":
    manager = AthleteManager()
    
    while True:
        print("Olympic Athlete Management System")
        print("1. Add Athlete Details")
        print("2. View Athlete Details")
        print("3. Delete Athlete Record")
        print("4. Filter Medal Details")
        print("5. View Performance by Gender")
        print("6. View Event Details")
        print("7. Show Statistics")
        print("8. View Performance of All Athletes")
        print("9. Medal Count and Details")
        print("10. Exit")
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                manager.add_details()
            case 2:
                manager.view_details()
            case 3:
                manager.delete_record()
            case 4:
                manager.winner_detail()
            case 5:
                sex = input("Enter gender (Male/Female): ")
                manager.athlete_gender(sex)
            case 6:
                manager.event_details()
            case 7:
                manager.statistics()
            case 8:
                manager.athlete_performance()
            case 9:
                manager.medal_count_and_detail()
            case 10:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Try again.")
