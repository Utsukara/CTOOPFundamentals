# Task 1: Public Transportation Module

# Problem Statement: Develop a Bus class as part of a public transportation module. 
# Use class variables to represent common attributes like city name and base fare. 
# Implement instance variables for specific attributes like route number and passenger capacity.
# Expected Outcome: A Bus class with both class and instance variables, and a transportation 
# module to manage different bus routes. 
# A test script should demonstrate creating bus instances and accessing both class and 
# instance attributes.

class Bus:
    # Class variables (shared among all instances)
    city = "Generic City"
    base_fare = 2.50  # Assume base fare is $2.50

    def __init__(self, route, capacity):
        # Instance variables (unique to each instance)
        self.route = route
        self.capacity = capacity

    def calculate_fare(self, passengers):
        # Calculate total fare based on number of passengers
        return self.base_fare * passengers

    def __str__(self):
        # String representation of the Bus instance
        return (f"Route: {self.route}, Capacity: {self.capacity}, "
                f"City: {self.city}, Base Fare: ${self.base_fare:.2f}")

# Test script
if __name__ == "__main__":
    
    Bus.city = "Springfield"
    Bus.base_fare = 1.75

    bus1 = Bus(route=101, capacity=50)
    bus2 = Bus(route=102, capacity=30)

    print(bus1)
    print(bus2)

    print(f"Total fare for 10 passengers on route {bus1.route}: ${bus1.calculate_fare(10):.2f}")
    print(f"Total fare for 5 passengers on route {bus2.route}: ${bus2.calculate_fare(5):.2f}")
