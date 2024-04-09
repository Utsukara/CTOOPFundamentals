# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number
#  of participants. Implement a method add_participant that increases the count and a method 
# get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
# class Event:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

    def __str__(self):
        return f"Event: {self.name}, Date: {self.date}, Participants: {self.participant_count}"

def display_events(events):
    if events:
        print("\nCurrent Events:")
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event}")
    else:
        print("No events have been created yet.")

def main():
    events = []
    current_event = None

    while True:
        print("\n1. Create Event")
        print("2. Add Participant")
        print("3. Get Participant Count")
        print("4. Switch Event")
        print("5. Display All Events")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            current_event = Event(name, date)
            events.append(current_event)
            print(f"Event created: {current_event}")
        elif choice == 2:
            if current_event:
                current_event.add_participant()
                print(f"Participant added: {current_event}")
            else:
                print("No event selected. Please create or switch to an event first.")
        elif choice == 3:
            if current_event:
                print(f"Participant count: {current_event.get_participant_count()}")
            else:
                print("No event selected. Please create or switch to an event first.")
        elif choice == 4:
            display_events(events)
            if events:
                try:
                    event_number = int(input("Enter event number to switch to: ")) - 1
                    current_event = events[event_number]
                    print(f"Switched to event: {current_event}")
                except (IndexError, ValueError):
                    print("Invalid event number.")
        elif choice == 5:
            display_events(events)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
