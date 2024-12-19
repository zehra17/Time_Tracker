# Time Tracker

## Description
Time Tracker is a simple Python-based application that helps users track and log their daily activities. The application allows users to log the start and end time of various activities and provides a summary of time spent on each activity. It's ideal for personal productivity tracking or for keeping an eye on how much time is spent on different tasks throughout the day.

## Features
- Add activities with start and end times.
- View a summary of time spent on each activity.
- Track multiple activities within the same day.
- Save and load data between sessions.

## Requirements
- Python 3.x installed on your system.

## How to Run
1. Clone or download the project to your local machine.
2. Open the project folder in your terminal or preferred IDE.
3. Run the Python script with the following command:
   ```bash
   python time_tracker.py
   ```
4. Follow the instructions displayed on the terminal to:
   - Add a new activity.
   - View the time log for activities.

## Code Explanation
- **add_activity()**: Adds a new activity by capturing the start and end times.
- **view_activities()**: Displays a list of all recorded activities and the time spent on each.
- **save_data()**: Saves the activity logs to a file for future use.
- **load_data()**: Loads the activity logs from the saved file when the application is started.

## Example Usage

```bash
Welcome to Time Tracker!

1. Add Activity
2. View Activity Log
3. Exit
Choose an option: 1

Enter the name of the activity: Study
Enter the start time (HH:MM): 09:00
Enter the end time (HH:MM): 11:00

'Study' has been added to your time log.

1. Add Activity
2. View Activity Log
3. Exit
Choose an option: 2

Activity Log:
1. Study - 2 hours
```

## Future Improvements
- Implement the ability to track activities over multiple days.
- Add the option to edit or delete activities.
- Include graphical visualization of time spent on each activity.

## License
This project is licensed under the MIT License.
