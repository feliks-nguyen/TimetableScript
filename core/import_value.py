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
                if not (0 < self.days <= 7):
                    print("\nThere is only 7 days in a week!")
                    continue
                self.lessons = int(input("\nEnter number of sessions per day: "))
                break
            except ValueError:
                print("\nPlease enter a valid number!")

    def days_sessions(self):
        # Returns number of days in a week, and name of each sessions in a day.
        sessions = []
        for day in range(self.days):
            names = []
            for num in range(self.lessons):
                print(f"\nEnter data for day {day+1}:")
                name = str(input(f"\nEnter name for session {num+1}: "))
                names.append(name)
            sessions.append(names)

        # Make a dictionary : {'day' : [sessions of that day]}
        tables = dict(zip(heptad[: self.days], sessions))
        return tables
