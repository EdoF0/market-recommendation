import sys

file_in = "analisi-di-mercato-without-dotzero-small-filtered.csv"
file_out = "analisi-di-mercato-without-dotzero-small-filtered-id0.csv"

# max lines processed
line_cap = 10

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        # Python allows to read big files line by line as follows
        for i, line in enumerate(csv_in):

            if (line_cap > 0 and i >= line_cap):
                break

            if (i > 0):
                sys.stdout.write(f"\rProcessing line {i}")
                sys.stdout.flush()

            line = line.split(',')

            # print columns
            if (i == 0):
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")

            # bring userid, that is the last column, to the first column
            id = line.pop()
            id = id.strip() # remove \n
            line.insert(0, id)

            # save cleaned data
            csv_out.write(','.join(line) + '\n')
