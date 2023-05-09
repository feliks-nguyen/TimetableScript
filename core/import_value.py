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
import calendar

heptad = list(calendar.day_abbr)


class ImportValue:
    def __init__(self):
        while True:
            try:
                self.days = int(input("\nFor how many days in week? "))
                self.lessons = int(input("\nEnter number of sessions per day: "))
                break
            except Exception:
                print("Please enter a valid number!")

    def days_sessions(self):
        # Returns number of days in a week, and name of each sessions in a day.
        sessions = []
        for day in range(1, self.days + 1):
            names = []
            for num in range(1, self.lessons + 1):
                print(f"\nEnter data for day {day}:")
                name = str(input(f"\nEnter name for session {num}: "))
                names.append(name)
            sessions.append(names)

        # Make a dictionary : {'day' : [sessions of that day]}
        tables = dict(zip(heptad[: self.days], sessions))
        return tables
