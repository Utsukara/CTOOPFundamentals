# Task 1: File Handling for Building Records

# Problem Statement: Implement a system to handle building records using file operations. Create a Building class and write a script to save and load building details to and from a file.
# Code Example: Skeleton of the Building class.
# class Building:
#     def __init__(self, name, floors):
#         self.name = name
#         self.floors = floors
#     # Methods to save to file and load from file
# Expected Outcome: A complete Building class with methods for saving to and loading details from a file. A script demonstrating saving multiple buildings to a file and then reading them back into the program.

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    @staticmethod
    def save_all_buildings(buildings, filename):
        """Save all building data to a file, overwriting any existing file content."""
        with open(filename, 'w') as file:
            for building in buildings:
                file.write(f"{building.name},{building.floors}\n")

    @staticmethod
    def load_from_file(filename):
        """Load building data from a file and return a list of Building instances."""
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                building = Building(name, int(floors))
                buildings.append(building)
        return buildings

    def __str__(self):
        return f"{self.name} - {self.floors} floors"

def main():
    try:
        buildings = Building.load_from_file("buildings.txt")
    except FileNotFoundError:
        buildings = []

    while True:
        print("\n1. Add Building")
        print("2. Display Buildings")
        print("3. Save Buildings")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter building name: ")
            try:
                floors = int(input("Enter number of floors: "))
            except ValueError:
                print("Please enter a valid integer for floors.")
                continue
            building = Building(name, floors)
            buildings.append(building)
            print(f"Building added: {building}")
        elif choice == 2:
            if buildings:
                print("\nBuildings:")
                for index, building in enumerate(buildings, start=1):
                    print(f"{index}. {building}")
            else:
                print("No buildings have been added yet.")
        elif choice == 3:
            Building.save_all_buildings(buildings, "buildings.txt")
            print("Buildings saved to file.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
