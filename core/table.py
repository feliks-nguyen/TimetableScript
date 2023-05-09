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
from import_value import ImportValue


class TableData:
    def __init__(self) -> None:
        self.array = list()
        self.parts = list()

    def inputData(self):
        # Adds data to 2 lists
        while True:
            try:
                parts_num = int(input("\nEnter number of parts: "))
                for i in range(1, parts_num + 1):
                    part = input(f"\nEnter name for part {i}: ")
                    self.parts.append(part)
                break
            except Exception:
                print('Please enter a valid number!')

        for name in self.parts:
            print(f"\nEnter value for {name}:")
            value = ImportValue()
            tables = value.days_sessions()
            self.array.append(tables.copy())
            nest = dict(zip(self.parts, self.array))
        return nest
