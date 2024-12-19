import time
import datetime
import json

class TimeTracker:
    def __init__(self):
        self.tasks = []
        self.load_data()

    def start_task(self, task_name):
        task = {
            "name": task_name,
            "start_time": time.time(),
            "end_time": None
        }
        self.tasks.append(task)
        print(f"'{task_name}' task started...")

    def stop_task(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name and task["end_time"] is None:
                task["end_time"] = time.time()
                print(f"'{task_name}' task stopped.")
                break
        else:
            print(f"Task '{task_name}' not found or already stopped.")

    def show_report(self):
        print("\nTime Tracker Report:")
        for task in self.tasks:
            if task["end_time"]:
                duration = task["end_time"] - task["start_time"]
                duration_str = str(datetime.timedelta(seconds=duration))
                print(f"Task: {task['name']}, Duration: {duration_str}")
            else:
                print(f"Task: {task['name']} is still running.")

    def save_data(self):
        with open("time_tracker_data.json", "w") as file:
            json.dump(self.tasks, file)
            print("Data saved successfully.")

    def load_data(self):
        try:
            with open("time_tracker_data.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")

def main():
    tracker = TimeTracker()

    while True:
        print("\n1. Start Task")
        print("2. Stop Task")
        print("3. Show Report")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            tracker.start_task(task_name)

        elif choice == "2":
            task_name = input("Enter task name: ")
            tracker.stop_task(task_name)

        elif choice == "3":
            tracker.show_report()

        elif choice == "4":
            tracker.save_data()

        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
