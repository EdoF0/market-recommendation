import sys
from os import path
from os import mkdir

file_in = "market.csv"
folder_out = "market-horizontal-split-test"

# max lines processed
line_cap = 10

# number of lines in each file, without the header
lines = 1000000
line_counter = 0
header = ""

# create output folder
if not path.exists(folder_out):
    mkdir(folder_out)

def generate_filename(file_index: int):
    return(f"market-{file_index}.csv")

# current output file related variables
file_index = 0
file_name = generate_filename(file_index)
file_out = None # None means that the previous file was closed

with open(file_in, "r") as csv_in:
    # Python allows to read big files line by line as follows
    for i, line in enumerate(csv_in):

        # apply line cap
        if (line_cap > 0 and i >= line_cap):
            break

        # log the current status
        if (i > 0):
            # line_counter+1 because of the header
            # spaces are needed to overwrite the whole number after line counter from millions becomes 1
            sys.stdout.write(f"\rInserting line {i} in file {file_name} line {line_counter+1}       ")
            sys.stdout.flush()

        # save the header in order to copy it in all the output files
        if (i == 0):
            header = line

        if (line_counter > lines):
            file_out.close()
            file_out = None

        if (file_out == None):
            file_index += 1
            file_name = generate_filename(file_index)
            file_out = open(f"{folder_out}/{file_name}", "w")
            file_out.write(header)
            line_counter = 0

        # avoid writing the header two times in the first file
        if (i != 0):
            file_out.write(line)
            line_counter += 1

if (file_out != None):
    file_out.close()
