import sys

file_in = "market-cleanup.csv"
file_out = "market-cleanup-grouped-test.csv"

# max lines processed
line_cap = 10

# list of column groups to sum for cleaned file
column_groups = {
    "time1": list(range(1, 9)),
    "time2": list(range(9, 16)),
    "length": list(range(16, 25)),
    "categories1": list(range(25, 56)),
}

# list of column groups to sum for original file
#column_groups = {
#    "time1": list(range(1-1, 9-1)),
#    "time2": list(range(9-1, 16-1)),
#    "length": list(range(16-1, 25-1)),
#    "categories1": list(range(25-1, 56-1)),
#    "categories2": list(range(56-1, 416-1)),
#    "categories3": list(range(416-1, 991-1)),
#    "sentiments1": list(range(991-1, 995-1)),
#    "feelings1": list(range(995-1, 1104-1)),
#}

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            # apply line cap
            # line cap 1 will stop after processing only the header
            if (line_cap > 0 and i >= line_cap):
                break

            # this will log the current line,
            # \r set the cursor to the beginning of the line in order to overwrite it and not printing millions of "Clearing line i"
            if (i > 0):
                sys.stdout.write(f"\rGrouping columns of line {i}")
                sys.stdout.flush()

            # get array of all columns
            line = line.split(',')
            # future output line
            line_grouped = []

            if (i > 0):
                for column_group_name in column_groups:
                    s = sum([float(line[j]) for j in column_groups[column_group_name]])
                    line_grouped.append(s)

            elif (i == 0):
                # print columns
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name}")
                # write header
                line_grouped = list(column_groups.keys())

            csv_out.write(','.join(str(value) for value in line_grouped) + '\n')
