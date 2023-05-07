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


from tabulate import tabulate
from import_value import ImportValue
from pathlib import Path

array = []
parts = []


def input_data():
    # Adds data to 2 lists
    parts_num = int(input("\nEnter number of parts: "))
    for i in range(1, parts_num + 1):
        part = input(f"\nEnter name for part {i}: ")
        parts.append(part)
    for name in parts:
        print(f"\nEnter value for {name}:")
        value = ImportValue(
            int(input("\nFor how many days in week? ")),
            int(input("\nEnter number of sessions per day: ")),
        )
        name, sessions = value.days_sessions()
        table = dict(zip(name, sessions))
        array.append(table.copy())


input_data()

nest = dict(zip(parts, array))

current_path = Path.cwd()

# Exports result into a file
with open(f"{current_path.parent}\\result.txt", "w", encoding="utf-8") as f:
    for part, table in nest.items():
        f.write(f"\n\nTABLE FOR {part.upper()}")
        f.write(
            f'\n{tabulate(table, headers="keys", showindex="always", tablefmt="fancy_grid")}'
        )
        f.write("\n\n\n ")
        f.close()
