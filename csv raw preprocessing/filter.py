import sys

file_in = "market.csv"
file_out = "market-clean-test.csv"
file_out_sum = "market-sum-test.csv" # if None does not write the sum csv

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

# returns True if the check_sum test was passed by the input line, False otherwise
def check_sum(line: list[str], margin: float = default_margin) -> bool:
    # keep track of single column groups outcome
    test_passed = True
    # list of sum value for each column group
    values_sum: list[float] = []

    # sum to 100 check
    for col_group_name in sum_to_100_col_groups:
        # sum each number in the line where the indexes are provided by the sum_to_100_col_groups list
        s = sum([float(line[j]) for j in sum_to_100_col_groups[col_group_name]])
        values_sum.append(s)
        # real check
        if not (s > (100-margin) and s < (100+margin)):
            test_passed = False
            # do not break here, because otherwise values_sum cannot be populated
    
    # sum less then 100 check
    for col_group_name in sum_lt_100_col_groups:
        # sum each number in the line where the indexes are provided by the sum_to_100_col_groups list
        s = sum([float(line[j]) for j in sum_lt_100_col_groups[col_group_name]])
        values_sum.append(s)
        # real check
        if not (s < (100+margin)):
            test_passed = False
            # do not break here, because otherwise values_sum cannot be populated
    
    # save values_sum to file
    write_sum(values_sum)
    return(test_passed)

# save for each row the sum of each column group
# this file can be useful to analyze the distribution of wrong sums
csv_out_sum = None
if file_out_sum != None:
    # if None the sum csv should not be written
    csv_out_sum = open(file_out_sum, "w")
# set sum csv header
header_sum: list = list(sum_to_100_col_groups.keys()) + list(sum_lt_100_col_groups.keys())

# function that does not fail write if file_out_sum is None
def write_sum(values: list) -> None:
    if file_out_sum != None and len(header_sum) == len(values):
        csv_out_sum.write(','.join(str(value) for value in values))

write_sum(header_sum)

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
                # writing \n is not needed since userid value includes the new line
                csv_out.write(','.join(line))
            else:
                lines_filtered += 1

# close the sum csv file with the exact same condition of opening it
if file_out_sum != None:
    csv_out_sum.close()
