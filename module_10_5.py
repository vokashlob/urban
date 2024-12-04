from time import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        # for line in file:
        #     all_data.append(line)
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# линейный вызов

# start_time1 = time()
#
# for filename in filenames:
#     read_info(filename)
#
# end_time1 = time()
# print(end_time1 - start_time1)

# многопроцессорный вызов

if __name__ == '__main__':
    start_time2 = time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
        end_time2 = time()
        print(end_time2 - start_time2)
