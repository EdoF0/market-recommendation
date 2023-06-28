import sys

file_in = "market.csv"
file_out = "market-with-sum-columns.csv"

# max lines processed
line_cap = 10

# new column generator functions called per-row

def sum_index(list, index_list):
    return sum([float(list[i]) for i in index_list])

new_columns = {
    "sum_time1": lambda row: str(sum_index(row, list(range(1, 9)))),
    "sum_time2": lambda row: str(sum_index(row, list(range(9, 16)))),
    "sum_length": lambda row: str(sum_index(row, list(range(16, 25)))),
    "sum_categories1": lambda row: str(sum_index(row, list(range(25, 56)))),
    "sum_categories2": lambda row: str(sum_index(row, list(range(56, 416)))),
    "sum_categories3": lambda row: str(sum_index(row, list(range(416, 991)))),
}

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            # apply line cap
            if (line_cap > 0 and i >= line_cap):
                break

            # log the current line
            if (i > 0):
                sys.stdout.write(f"\rAdding columns from line {i}")
                sys.stdout.flush()

            line = line.split(',')
            # remove \n from last line
            line[-1] = line[-1].strip()

            # print columns and add new columns
            if (i == 0):
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")
                for name in new_columns.keys():
                    line.append(name)
                    print(f"{j} [new] {name}")

            # new columns
            else:
                for col_function in new_columns.values():
                    value = col_function(line)
                    # remove .0 that is useless
                    if value.endswith(".0"):
                        value = value[:-2]
                    line.append(value)

            # save data
            csv_out.write(','.join(line) + '\n')
