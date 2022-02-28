import sys
import os
import csv
import time

start_time = time.time()
input_file = sys.argv[1]
output_file = sys.argv[2]
min_dist = float(sys.argv[3])
max_dist = float(sys.argv[4])

def find_ideal():
    #open input and output files
    total_rows = 0
    discarded_rows = 0
    
    with open(os.path.expanduser(input_file), newline='') as re, open(os.path.expanduser(output_file), "x") as wr:
        #loop through the input file
        for row in csv.reader(re, delimiter=","):
            #write rows that match criteria
            if (float(row[-1]) >= min_dist and float(row[-1]) <= max_dist):
                    wr.write(",".join(row) + "\n")
            else:
                discarded_rows += 1
            total_rows += 1
    print("Total Rows:", (total_rows))
    print("Discarded Rows:", (discarded_rows))
    print("% within desired range:", (discarded_rows/total_rows*100))
    print("Execution time in seconds:", (time.time() - start_time))

def main():
    find_ideal()

if __name__ == "__main__":
    main()