# MIT License

# Copyright (c) 2023 Nghia Nguyen

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
                print(f"\nEnter data for day {day}:")
                name = str(input(f"\nEnter name for session {num}: "))
                names.append(name)
            day_sessions.append(names)

        # Convert day numbers and day names into a dictionary.
        day_list = dict(zip(num_day, day_name[: self.week_days]))
        day_value = []
        for day in day_list.values():
            # Get the day name, and add it to a list.
            day_value.append(day)
        return day_value, day_sessions
