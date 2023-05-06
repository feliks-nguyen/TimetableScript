from tabulate import tabulate
from import_value import ImportValue

array = []
parts = []


def input_data():
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

for part, table in nest.items():
    print(f"\n\nTABLE FOR {part.upper()}")
    print(
        f'\n{tabulate(table, headers="keys", showindex="always", tablefmt="fancy_grid")}'
    )
