import sys
import os
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
min_dist = float(sys.argv[3])
max_dist = float(sys.argv[4])

def find_ideal():
    #open input and output files
    re = open(os.path.expanduser(input_file), newline='')
    wr = open(os.path.expanduser(output_file), "x")
    #create reader object on the open file
    file_reader = csv.reader(re, delimiter=",")
    #loop through the file to find target rows
    for row in file_reader:
        if (float(row[6]) >= min_dist and float(row[6]) <= max_dist):
                wr.write(",".join(row) + "\n")

def main():
    find_ideal()

if __name__ == "__main__":
    main()