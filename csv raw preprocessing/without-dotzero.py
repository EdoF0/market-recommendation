import sys

file_in = "analisi-di-mercato.csv"
file_out = "analisi-di-mercato-without-dotzero.csv"

# max lines processed
line_cap = 10

zero_as_null = False

with open(file_out, "w") as csv_out:
    with open(file_in, "r") as csv_in:
        for i, line in enumerate(csv_in):

            # apply line cap
            if (line_cap > 0 and i >= line_cap):
                break

            # print progress
            if (i > 0):
                sys.stdout.write(f"\rCleaning line {i}")
                sys.stdout.flush()

            line = line.split(',')

            for j, value in enumerate(line):
                
                # remove .0 that is useless
                if value.endswith(".0"):
                    line[j] = value[:-2]

                # remove 0 values completely
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

            csv_out.write(','.join(line))
