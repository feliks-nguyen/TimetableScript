day_name = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


class ImportValue:
    def __init__(self, week_days, day_session_nums):
        self.week_days = week_days
        self.day_session_nums = day_session_nums

    def days_sessions(self):
        # Returns number of days in a week, and name of each sessions in a day.
        num_day = []
        day_sessions = []
        for day in range(1, self.week_days + 1):
            num_day.append(day)
            names = []
            for num in range(1, self.day_session_nums + 1):
                print(f"\nInsert data for day {day}:")
                name = str(input(f"\nInsert name for session {num}: "))
                names.append(name)
            day_sessions.append(names)

        # Convert day numbers and day names into a dictionary.
        day_list = dict(zip(num_day, day_name[: self.week_days]))
        day_value = []
        for day in day_list.values():
            # Get the day name, and add it to a list.
            day_value.append(day)
        return day_value, day_sessions
