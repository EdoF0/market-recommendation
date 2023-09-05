import sys

file_in = "analisi-di-mercato.csv"
file_out = "analisi-di-mercato-zeros-columns.csv"

# max lines processed
line_cap = 10

# columns to analyze
columns = list(range(0, 1103)) # all but id

# keep track of progress with a map
nonzero_count = {}

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            if (line_cap > 0 and i >= line_cap):
                break

            if (i > 0):
                sys.stdout.write(f"\rProcessing line {i}")
                sys.stdout.flush()

            line = line.split(',')

            if (i == 0):
                col_names = []
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")
                    if j in columns:
                        nonzero_count[j] = 0
                        col_names.append(col_name.strip())
                csv_out.write(','.join(col_names) + '\n')
            else:
                for j in columns:
                    value = float(line[j])
                    if value != 0:
                        nonzero_count[j] += 1

        # save values
        csv_out.write(','.join([str(nonzero_count[j]) for j in columns]) + '\n')
