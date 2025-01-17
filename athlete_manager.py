from data import olympic_list
from tabulate import tabulate
class AthleteManager:

    def add_details(self):
        record = int(input("Enter limit: "))
        for i in range(record):
            year = int(input("Enter the year of Olympic: "))
            name = input("Enter the athlete name: ")
            age = int(input("Enter the athlete age: "))
            sex = input("Enter the sex of player: ")
            height = float(input("Enter the athlete height in cm: "))
            weight = float(input("Enter the athlete weight in kg: "))
            medal = int(input("Enter the medal won in that year: "))
            medaltype = input("Enter the type of medal won by the athlete: ")
            sport = input("Enter the sport: ")
            country = input("Enter which country participated: ")
            event = input("In which country Olympic was conducted: ")
            time = float(input("Enter the time taken by the athlete to complete this game in hrs: "))
            distance = float(input("Enter the distance of track in km: "))
            
            olympic_list.append(
                {
                    'Year': year,
                    'Athlete Name': name,
                    'Age': age,
                    'Sex': sex,
                    'Height(in cm)': height,
                    'Weight': weight,
                    'Medal': medal,
                    'Medal_Type': medaltype,
                    'Sport': sport,
                    'Country': country,
                    'Event': event,
                    'Time(in hrs)': time,
                    'Distance(in km)': distance
                }
            )

    def delete_record(self):
        year_delete = int(input("Enter the year of the Olympic event you want to delete: "))
        matching_records = [record for record in olympic_list if record['Year'] == year_delete]
        
        if not matching_records:
            print(f"No records found for the year {year_delete}.")
            return
        
        print(f"Records found for the year {year_delete}:")
        for i, record in enumerate(matching_records, start=1):
            print(f"\nRecord {i}:")
            for key, value in record.items():
                # print(f"{key}: {value}")
                print(tabulate([[key, value]],tablefmt='grid'))

        record_number = int(input(f"Enter the record number (1-{len(matching_records)}) you want to delete: "))
        
        if 1 <= record_number <= len(matching_records):
            record_delete = matching_records[record_number - 1]
            confirm = input(f"Are you sure you want to delete the record for {record_delete['Athlete Name']}? (yes/no): ")
            
            if confirm.lower() == 'yes':
                olympic_list.remove(record_delete)
                print("Record deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print("Invalid record number.")

    def view_details(self):
        header =['\033[1mYear\033[0m','\033[1mAthlete Name\033[0m','\033[1mAge\033[0m','\033[1mSex\033[0m','\033[1mHeight(in cm)\033[0m','\033[1mWeight\033[0m','\033[1mMedal\033[0m','\033[1mMedal_Type\033[0m','\033[1mSport\033[0m','\033[1mCountry\033[0m']
        row=[[
                data['Year'],data['Athlete Name'],data['Age'],data['Sex'],data['Height(in cm)'],data['Weight'],data['Medal'],data['Medal_Type'],data['Sport'],data['Country']
            ]
            for data in olympic_list]
        print(tabulate(row,header,tablefmt="fancy_grid"))

    def medal_details(self, medal_type):
        print(f"Details of athletes who won {medal_type} medals:\n")
        header = ['\033[1mYear\033[0m','\033[1mAthlete Name\033[0m','\033[1mAge\033[0m','\033[1mSex\033[0m','\033[1mHeight(in cm)\033[0m']
        row = [[data['Year'],data['Athlete Name'],data['Age'],data['Sex'],data['Height(in cm)']]
                    for data in olympic_list if data['Medal_Type'] == medal_type
                ]
        print(tabulate(row,header,tablefmt="fancy_grid"))
        print()    

    def winner_detail(self):
        print("To know about winners according to medal, choose from below:")
        print("1. Gold Medal\n2. Silver Medal\n3. Bronze Medal")
        select = int(input("Select Your Choice: "))
        
        match select:
            case 1:
                self.medal_details("Gold")
            case 2:
                self.medal_details("Silver")
            case 3:
                self.medal_details("Bronze")
            case _:
                print("Invalid choice.")

    def medal_count_and_detail(self):
        total_medals = sum(data['Medal'] for data in olympic_list)
        print(f"Total number of medals: {total_medals}")
        print("To know about any medal, choose from below:")
        print("1. Gold Medal\n2. Silver Medal\n3. Bronze Medal")
        select = int(input("Select Your Choice: "))
        
        match select:
            case 1:
                self.medal_details("Gold")
            case 2:
                self.medal_details("Silver")
            case 3:
                self.medal_details("Bronze")
            case _:
                print("Invalid choice.")

    def athlete_gender(self, sex):
        header = ['\033[1mAthlete Name\033[0m','\033[1mSex\033[0m','\033[1mSport\033[0m','\033[1mTime(in hrs)\033[0m','\033[1mDistance(in km)\033[0m']
        row = [[ data['Athlete Name'],data['Sex'],data['Sport'],data['Time(in hrs)'],data['Distance(in km)']]
                for data in olympic_list if data['Sex'].lower() == sex.lower()
                ]
        print(tabulate(row,header,tablefmt="fancy_grid"))
        print()
        
    def athlete_performance(self):
        header =['\033[1mAthlete Name\033[0m','\033[1mSex\033[0m','\033[1mSport\033[0m','\033[1mTime(in hrs)\033[0m','\033[1mDistance(in km)\033[0m']
        row=[[
                data['Athlete Name'],data['Sex'],data['Sport'],data['Time(in hrs)'],data['Distance(in km)']
            ]   
            for data in olympic_list]
        print(tabulate(row,header,tablefmt="fancy_grid"))

   

    def event_details(self):
        header = ['\033[1mYear\033[0m', '\033[1mAthlete Name\033[0m', '\033[1mMedal_Type\033[0m','\033[1mSport\033[0m', '\033[1mCountry\033[0m', '\033[1mEvent\033[0m']
        row = [[
                data['Year'], data['Athlete Name'], data['Medal_Type'],data['Sport'], data['Country'], data['Event']
            ]
            for data in olympic_list
        ]
        print(tabulate(row, header, tablefmt="fancy_grid"))


    def statistics(self):
        total_time = sum(data['Time(in hrs)'] for data in olympic_list)
        stats1=[["Total time taken in hrs:",f"{total_time:.2f}"]]
        print(tabulate(stats1,tablefmt="fancy_grid"))
        total_distance = sum(data['Distance(in km)'] for data in olympic_list)
        stats2=[["Total distance in km:",f"{total_distance:.2f}"]]
        print(tabulate(stats2,tablefmt="fancy_grid"))
        average_speed = total_distance / total_time
        stats3=[["Average speed is:",f"{average_speed:.2f} km/h"]]
        print(tabulate(stats3,tablefmt="fancy_grid"))
        print("\n")
