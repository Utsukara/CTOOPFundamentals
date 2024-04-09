# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, 
# and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few 
# instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
# class Vehicle:
#     def __init__(self, reg_num, type, owner):
#         self.registration_number = reg_num
#         self.type = type
#         self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and 
# a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Type: {self.type}, Owner: {self.owner}"

def main():
    vehicles = []

    while True:
        print("\n1. Create Vehicle")
        print("2. Update Owner")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            reg_num = input("Enter registration number: ")
            vehicle_type = input("Enter vehicle type: ")
            owner = input("Enter owner name: ")
            vehicle = Vehicle(reg_num, vehicle_type, owner)
            vehicles.append(vehicle)
            print(f"Vehicle created: {vehicle}")
        elif choice == 2:
            if vehicles:
                reg_num = input("Enter the registration number of the vehicle to update: ")
                matched_vehicles = [v for v in vehicles if v.registration_number == reg_num]
                if matched_vehicles:
                    new_owner = input("Enter new owner name: ")
                    matched_vehicles[0].update_owner(new_owner)
                    print(f"Owner updated: {matched_vehicles[0]}")
                else:
                    print("No vehicle found with that registration number.")
            else:
                print("No vehicles have been created yet.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

