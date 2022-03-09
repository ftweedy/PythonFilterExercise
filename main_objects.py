import sys
import os
import time

class Filter:
    # initialize values in new object
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

        self.read_data()  # self.data

    def read_data(self):
        with open(os.path.expanduser(self.input_file), newline='') as f:
            self.data = f.readlines()

    @staticmethod
    def filter_by_distance_column(data: list, min_dist: int, max_dist: int) -> list:
        result = []

        for line in data:
            distance = int(line.split(",")[-1])
            if min_dist <= distance <= max_dist:
                result.append(line)

        return result

    def write_data(self, data: list) -> None:
        with open(self.output_file, 'w') as f:
            for line in data:
                f.write(line)

def main():
    filter = Filter(sys.argv[1], sys.argv[2])
    data = filter.data

    filtered_data = filter.filter_by_distance_column(data, int(sys.argv[3]), int(sys.argv[4]))
    filter.write_data(filtered_data)

    print(f"Total Rows: {len(data)}")
    print(f"Discarded Rows: {len(data) - len(filtered_data)}")
    print(f"% within desired range: {len(filtered_data)/len(data)*100}")

    # filtered_data = filter.filter_by_distance_column(data, 3, 4)
    # filtered_data = filter.filter_by_x_column(filtered_data, 1, 2)

    # filter.write_data(filtered_data)


if __name__ == "__main__":
    main()

    # @staticmethod
    # def filter_by_x_column(data: list, min_x: int, max_x: int) -> list:
    #     result = []

    #     for line in data:
    #         x = int(line.split(",")[5])
    #         if min_x <= distance <= max_x:
    #             result.append(line)

    #     return result

    # def write_data(self, data: list, min_x, max_x) -> None:
    #     with open(self.output_file, 'w') as f:
    #         for line in data:
    #             if (min_x <=  <= max_x):
    #                 f.write(line)

    # use filter values to filter
    # def filter_by_distance_column(self, min_dist, max_dist):
    #     # initialize timer and unpackage self values
    #     start_time = time.time()
    # 
    #     # open input and output files
    #     with open(os.path.expanduser(input_file), newline='') as re, open(os.path.expanduser(output_file), "x") as wr:
    #         # loop through the input file and write to output file while incrementing row counters
    #         for row in csv.reader(re, delimiter=","):
    #             if (float(row[-1]) >= min_dist and float(row[-1]) <= max_dist):
    #                 wr.write(",".join(row) + "\n")
    #             else:
    #                 discarded_rows += 1
    #             total_rows += 1
    #     # print all the results
    #     print(f"Total Rows: {total_rows}")
    #     print(f"Discarded Rows: {discarded_rows}")
    #     print(f"% within desired range: {discarded_rows / total_rows * 100}")
    #     print(f"Execution time in seconds: {time.time() - start_time}")