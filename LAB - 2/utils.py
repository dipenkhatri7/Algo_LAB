import time
# Importing time module for measuring execution time
import matplotlib.pyplot as plt
# Importing matplotlib for plotting
import random
# Importing random module for generating random lists

def randomListAndTime(sorting_function, start, end, step):
    sizes = []
    execution_times = []
    for i in range(start, end + 1, step):
        random_list = [random.randint(0, 1000) for _ in range(i)] 
        # Generate a random list of size i
        sizes.append(i) 
        # Append the size to sizes list
        execution_time = measureExecutionTime(sorting_function, random_list, 0, len(random_list) - 1)
        # Measure execution time
        execution_times.append(execution_time) 
        # Append execution time to execution_times list
    return sizes, execution_times

def measureExecutionTime(sort_algo, A, low, high):

    start_time = time.time() 
    # Record start time
    sort_algo(A,low,high) 
    # Execute the sorting algorithm
    end_time = time.time() 
    # Record end time
    return end_time - start_time 
    # Return the elapsed time

def plotPerformance(sizes, times, label):

    plt.plot(sizes, times, label=label) 
    # Plot input sizes vs execution times
    plt.xlabel('Input Size') 
    # Set label for x-axis
    plt.ylabel('Execution Time (s)') 
    # Set label for y-axis
    plt.title('Input Size vs Execution Time') 
    # Set title for the plot
    plt.legend() 
    # Show legend
    plt.show() 
    # Display the plot
