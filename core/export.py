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
from pathlib import Path
import pandas as pd
from tabulate import tabulate
from table import TableData

nest = TableData().inputData()


def exportTXT(filename):
    """export the table into a <given name>.txt file"""
    # Define the file name and path
    file_path = Path.cwd().parent / "results" / f"{filename}.txt"
    with open(f"{file_path}", "w", encoding="utf-8") as f:
        # Loop over the nested dictionary and create a dataframe for each table
        for part, table in nest.items():
            # Write the dataframe to a sheet in the TXT file
            df = pd.DataFrame(table)
            df.index += 1
            f.write(f"\n\nTABLE FOR {part.upper()}")
            f.write(
                f'\n{tabulate(df, headers="keys", showindex="always", tablefmt="fancy_grid")}'
            )
            f.write("\n\n\n ")
        f.close()


def exportXLSX(filename):
    """export the table into a <given name>.xlsx file"""
    # Define the file name and path
    file_path = Path.cwd().parent / "results" / f"{filename}.xlsx"

    # Create an ExcelWriter object
    with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
        # Loop over the nested dictionary and create a dataframe for each table
        for part, table in nest.items():
            df = pd.DataFrame(table)
            df.index += 1
            # Write the dataframe to a sheet in the Excel file
            df.to_excel(writer, sheet_name=part.capitalize())


def main():
    print('Chose your export file type:\nEnter "1" for: txt\nEnter "2" for: xlsx')
    while True:
        mode = input()

        if mode == "1":
            exportTXT(input("Enter file name: "))
            break
        elif mode == "2":
            exportXLSX(input("Enter file name: "))
            break
        else:
            print("Invalid file format! Please try again.")

#Run the main program
if __name__ == "__main__":
	main()
