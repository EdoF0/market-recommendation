import sys
from os import path
from os import mkdir

file_in = "market.csv"
folder_out = "market-vertical-split-test"

# max lines processed
line_cap = 10

# lists of columns partitions with csv filename as key
col_groups = {
    "time1": list(range(0, 8)), # time1
    "time2": list(range(8, 15)), # time2
    "length": list(range(15, 24)), # length
    "categories1": list(range(24, 55)), # categories1
    "categories2": list(range(55, 415)), # categories2
    "categories3": list(range(415, 990)), # categories3
}
# column to use as id, to add to every partition / column group
id_idx = 990
id_column_name = "userid"

# functions for generating new column names, the input is the old column name
# all the functions strip the column group name and the following underscore from original names
col_name_transform = {
    "time1": lambda col_name: col_name[6:], # time1
    "time2": lambda col_name: col_name[6:], # time2
    "length": lambda col_name: col_name[1:], # length
    "categories1": lambda col_name: col_name[12:], # categories1
    "categories2": lambda col_name: col_name[12:], # categories2
    "categories3": lambda col_name: col_name[12:], # categories3
}

# create output folder
if not path.exists(folder_out):
    mkdir(folder_out)

# open output files
files_out = {}
for group_name in col_groups:
    files_out[group_name] = open(f"{folder_out}/{group_name}.csv", "w")

with open(file_in, "r") as csv_in:
    # Python allows to read big files line by line as follows
    for i, line in enumerate(csv_in):

        # apply line cap
        if (line_cap > 0 and i >= line_cap):
            break

        # log the current status
        if (i > 0):
            sys.stdout.write(f"\rSplitting line {i}")
            sys.stdout.flush()

        # get array of all columns
        line = line.split(',')
        
        # split
        for group_name in col_groups:
            # get the values for the given group
            selected_values = [line[j] for j in col_groups[group_name]]
            # ad the id column
            # if dealing with the csv header, also transform the column names with the provided function
            if (i == 0):
                for k, value in enumerate(selected_values):
                    selected_values[k] = col_name_transform[group_name](value)
                selected_values.insert(0,id_column_name)
            else:
                selected_values.insert(0,line[id_idx].strip())
            # write to file
            files_out[group_name].write(','.join(selected_values)+'\n')

        # print columns
        if (i == 0):
            for j, col_name in enumerate(line):
                print(f"{j} {col_name}")

for name in files_out:
    files_out[name].close()
