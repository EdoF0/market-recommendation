import sys

file_in = "analisi-di-mercato.csv"
file_out = "analisi-di-mercato-zeros.csv"

# max lines processed
line_cap = 10

# columns to analyze
columns = list(range(0, 1103)) # all but id

# keep track of progress
sum_lt_zero = 0
sum_zero = 0
sum_gt_zero = 0

negative_numbers = 0
zero_numbers = 0
positive_numbers = 0

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
                for j, col_name in enumerate(line):
                    print(f"{j} {col_name.strip()}")
            else:
                sum = 0
                for j in columns:
                    value = float(line[j])
                    sum += value
                    if value == 0:
                        zero_numbers += 1
                    elif value < 0:
                        negative_numbers += 1
                    else:
                        positive_numbers += 1
                
                if sum == 0:
                    sum_zero += 1
                elif sum < 0:
                    sum_lt_zero += 1
                else:
                    sum_gt_zero += 1

        # save values
        csv_out.write(f"sum_lt_zero,sum_zero,sum_gt_zero,negative_numbers,zero_numbers,positive_numbers\n{str(sum_lt_zero)},{str(sum_zero)},{str(sum_gt_zero)},{str(negative_numbers)},{str(zero_numbers)},{str(positive_numbers)}\n")
