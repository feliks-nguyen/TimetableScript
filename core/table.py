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
