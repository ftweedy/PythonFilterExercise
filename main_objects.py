import sys
import os
import csv
import time

class find_ideal:
    def __init__(self, input_file, output_file, min_dist, max_dist):
        self.input_file = input_file
        self.output_file = output_file
        self.min_dist = min_dist
        self.max_dist = max_dist
        self.total_rows = 0
        self.discarded_rows = 0
    
    def execute(self):
        start_time = time.time()
        (input_file, output_file, min_dist, max_dist, total_rows, discarded_rows) = (self.input_file, self.output_file, self.min_dist,  self.max_dist, self.total_rows, self.discarded_rows)
        
        with open(os.path.expanduser(input_file), newline='') as re, open(os.path.expanduser(output_file), "x") as wr:
            #loop through the input file
            for row in csv.reader(re, delimiter=","):
                #write rows that match criteria
                if (float(row[-1]) >= min_dist and float(row[-1]) <= max_dist):
                        wr.write(",".join(row) + "\n")
                else:
                    discarded_rows += 1
                total_rows += 1
        print(f"Total Rows: {total_rows}")
        print(f"Discarded Rows: {discarded_rows}")
        print(f"% within desired range: {discarded_rows/total_rows*100}")
        print(f"Execution time in seconds: {time.time() - start_time}")

def main():
    initialized = find_ideal(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
    initialized.execute()

if __name__ == "__main__":
    main()