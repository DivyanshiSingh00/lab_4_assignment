class FlightTable:
    def __init__(self):
        self.data = [
            ["Mumbai", "India", "Sri Lanka", "DAY"],
            ["Delhi", "England", "Australia", "DAY-NIGHT"],
            ["Chennai", "India", "South Africa", "DAY"],
            ["Indore", "England", "Sri Lanka", "DAY-NIGHT"],
            ["Mohali", "Australia", "South Africa", "DAY-NIGHT"],
            ["Delhi", "India", "Australia", "DAY"]
        ]

    def search_by_team(self, team_name):
        matches = []
        for match in self.data:
            if team_name in match[1] or team_name in match[2]:
                matches.append(match)
        return matches

    def search_by_location(self, location):
        matches = []
        for match in self.data:
            if location == match[0]:
                matches.append(match)
        return matches

    def search_by_timing(self, timing):
        matches = []
        for match in self.data:
            if timing == match[3]:
                matches.append(match)
        return matches

    def display_matches(self, matches):
        if not matches:
            print("No matches found.")
        else:
            print("Location\tTeam 01\t\tTeam 02\t\tTiming")
            for match in matches:
                print(f"{match[0]}\t\t{match[1]}\t\t{match[2]}\t\t{match[3]}")

def main():
    flight_table = FlightTable()

    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            team_name = input("Enter Team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.display_matches(matches)
        elif choice == 2:
            location = input("Enter Location: ")
            matches = flight_table.search_by_location(location)
            flight_table.display_matches(matches)
        elif choice == 3:
            timing = input("Enter Timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.display_matches(matches)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
