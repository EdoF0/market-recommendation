import sys

file_in = "analisi-di-mercato-without-dotzero.csv"
file_out = "analisi-di-mercato-without-dotzero-small.csv"

# max lines processed
line_cap = 10

delete_columns = list(range(55, 1103)) # categories2, categories3, sentiments1, feelings1
# reverse because if deleting in order column indexes changes by one every time
delete_columns.reverse()

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            # apply line cap
            if (line_cap > 0 and i >= line_cap):
                break

            # log the current line
            if (i > 0):
                sys.stdout.write(f"\rDeleting columns from line {i}")
                sys.stdout.flush()

            line = line.split(',')

            # print columns
            if (i == 0):
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")

            # delete columns
            for column_index in delete_columns:
                del line[column_index]

            # save cleaned data
            csv_out.write(','.join(line))
