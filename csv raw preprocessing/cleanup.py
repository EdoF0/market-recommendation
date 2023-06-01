import sys

file_in = "analisi-di-mercato.csv"
file_out = "market-test.csv"

# max lines processed
line_cap = 10

# clean parameters
delete_columns = list(range(990, 1103)) # sentiments1 and feelings1 columns, that cannot be trusted
zero_as_null = False

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
                sys.stdout.write(f"\rCleaning line {i}")
                sys.stdout.flush()

            # get array of all columns
            line = line.split(',')

            for j, value in enumerate(line):
                
                # remove .0 that is useless
                if value.endswith(".0"):
                    line[j] = value[:-2]

                # remove 0 values because default value is already 0
                if (zero_as_null):
                    try:
                        value_number = float(value)
                        if (value_number == 0):
                            line[j] = ""
                    except ValueError:
                        # not a number, ok
                        value_number = 0 # just some code here because it's mandatory

            # print columns
            if (i == 0):
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")

            # delete columns
            for column_index in sorted(delete_columns, reverse=True):
                del line[column_index]

            # bring userid, that is the last column, to the first column
            id = line.pop()
            id = id.strip() # remove \n
            line.insert(0, id)

            # save cleaned data
            csv_out.write(','.join(line) + '\n')
