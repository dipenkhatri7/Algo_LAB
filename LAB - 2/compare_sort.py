# compare_sorts.py

import utils
from merge_sort import merge_sort
from quick_sort import quick_sort
import matplotlib.pyplot as plt

def compare_sorts():
    sizes, merge_sort_times = utils.randomListAndTime(merge_sort, 0, 1000, 10)
    _, quick_sort_times = utils.randomListAndTime(quick_sort, 0, 1000, 10)
    
    plt.plot(sizes, merge_sort_times, label="Merge Sort")
    plt.plot(sizes, quick_sort_times, label="Quick Sort")
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Input Size vs Execution Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    compare_sorts()
