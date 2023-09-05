import sys

file_in = "analisi-di-mercato-without-dotzero-small-filtered-id0-sumcols.csv"
file_out = "analisi-di-mercato-without-dotzero-small-filtered-id0-sumcols-sumfiltered.csv"

# max lines processed
line_cap = 10

# list of sum columns indices
columns = list(range(54, 58))
margin = 0.00000000000001

# keep track of filtered lines
lines_filtered = 0

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            # apply line cap
            if (line_cap > 0 and i >= line_cap):
                break

            # print progress
            if (i > 0):
                sys.stdout.write(f"\r{lines_filtered} lines filtered so far, cleaning line {i}")
                sys.stdout.flush()

            line = line.split(',')

            ok = True

            if (i == 0):
                # print columns
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name}")
            else:
                for j in columns:
                    ok = ok and float(line[j]) > 0 + margin
                    if not ok:
                        break

            # save cleaned data
            if (ok):
                # writing \n is not needed since last value includes the new line
                csv_out.write(','.join(line))
            else:
                lines_filtered += 1
