import sys

file_in = "market-cleanup.csv"
file_out = "market-cleanup-filter-test.csv"

# max lines processed
line_cap = 10

# custom functions to check the rows

default_margin = 1

# list of column groups in which columns should sum to 100%
sum_to_100_col_groups = {
    "time1": list(range(1, 9)),
    "time2": list(range(9, 16)),
    "length": list(range(16, 25)),
    "categories1": list(range(25, 56)),
}
# list of column groups in which columns should sum to less or equal 100%
sum_lt_100_col_groups = {
    "categories2": list(range(56, 416)),
    "categories3": list(range(416, 991)),
}
# list of column groups in which columns should sum greater than 0
sum_gt_0_col_groups = {
    "time1": list(range(1, 9)),
    "time2": list(range(9, 16)),
    "length": list(range(16, 25)),
    "categories1": list(range(25, 56)),
    "categories2": list(range(56, 416)),
    "categories3": list(range(416, 991)),
}

# returns True if the check_sum test was passed by the input line, False otherwise
def check_sum(line: list[str], margin: float = default_margin) -> bool:
    # sum to 100 check
    for col_group_name in sum_to_100_col_groups:
        # sum each number in the line where the indexes are provided by the sum_to_100_col_groups list
        s = sum([float(line[j]) for j in sum_to_100_col_groups[col_group_name]])
        # real check
        if not (s > (100-margin) and s < (100+margin)):
            return(False)
    
    # sum less then 100 check
    for col_group_name in sum_lt_100_col_groups:
        s = sum([float(line[j]) for j in sum_lt_100_col_groups[col_group_name]])
        if not (s < (100+margin)):
            return(False)
    
    # sum greater then 0 check
    for col_group_name in sum_gt_0_col_groups:
        s = sum([float(line[j]) for j in sum_gt_0_col_groups[col_group_name]])
        if not (s > 0):
            return(False)

    return(True)

# list of boolean functions with a line as input
# each one must return true in order to keep a row in the output file
checks = [
    check_sum,
]

# keep track of filtered lines
lines_filtered = 0

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        # Python allows to read big files line by line as follows
        for i, line in enumerate(csv_in):

            # apply line cap
            # line cap 1 will stop after processing only the header
            if (line_cap > 0 and i >= line_cap):
                break

            # this will log the current line,
            # \r set the cursor to the beginning of the line in order to overwrite it and not printing millions of "Clearing line i"
            if (i > 0):
                sys.stdout.write(f"\r{lines_filtered} lines filtered so far, cleaning line {i}")
                sys.stdout.flush()

            # get array of all columns
            line = line.split(',')

            # if this line can be written to the filtered file
            ok = True

            if (i > 0):
                for check_function in checks:
                    ok = ok and check_function(line)
                    if (ok == False):
                        break
            elif (i == 0):
                # print columns
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name}")

            # save cleaned data
            if (ok):
                # writing \n is not needed since last value includes the new line
                csv_out.write(','.join(line))
            else:
                lines_filtered += 1

