# MSCS532 Algorithms and Data Structures
# Assignment 5 - Quicksort Algorithm: Implementation, Analysis, and Randomization
# Shrisan Kapali
# Student Id: 005032249

# Importing random & time library
import random
import time
import sys
import matplotlib.pyplot as plt
import numpy as np

# Increasing the recursion limig
sys.setrecursionlimit(50000)


# Implementing Deterministic QuickSort partition method
def partition(array, low, high):
    # Selecting pivot as the lowest element
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        # For pointer i find the element at i that is greater than pivot
        while i <= j and array[i] <= pivot:
            i += 1
        # For pointer i find the element at j that is less than pivot
        while i <= j and array[j] > pivot:
            j -= 1
        # Swap i,j
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j


# Quick Sort Method
def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


# *****************************************************
# Implementing Randomized QuickSort
# *****************************************************


# Creating a method that implements randomized partition
def randomized_partition(array, low, high):
    # Using random pick a number between low, high
    pivotIndex = random.randint(low, high)
    # Swapping array at pivot with last element
    array[pivotIndex], array[high] = array[high], array[pivotIndex]
    # Select pivot as array at higher position
    pivot = array[high]
    # Starting pointer i at low-1 position
    i = low - 1

    # Loop pointer j from low to high
    for j in range(low, high):
        # For j is array at position j is less than pivot, swap
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap array at position i+1 with high
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


# Implementation of Quick Sort
def randomized_quicksort(array, low, high):
    if low < high:
        pivot = randomized_partition(array, low, high)
        # Left side partition
        randomized_quicksort(array, low, pivot - 1)
        # Right side partition
        randomized_quicksort(array, pivot + 1, high)


# Test cases of different array sizes and distributions
# Setting up the sizes
sizes = [500, 1000, 2500, 5000, 7500, 10000]
distributions = ["Sorted", "Reverse_Sorted", "Random"]

# Creating a list to store the quicksort time for each sort
executionTimeDeterministic = {dist: [] for dist in distributions}
executionTimeRandomized = {dist: [] for dist in distributions}


# Writing a function to perform quicksort and measure the time
def measure_time(function, array):
    start = time.time()
    function(array, 0, len(array) - 1)
    end = time.time()
    return end - start


# Looping through all the sizes
for size in sizes:
    # For each distribution generate the data sets
    for dist in distributions:
        if "Sorted" == dist:
            data = list(range(size))
        elif "Reverse_Sorted" == dist:
            data = list(range(size, 0, -1))
        elif "Random" == dist:
            data = random.sample(range(size), size)

        # Perform Deterministic quick sort
        start = time.time()
        quicksort(data.copy(), 0, len(data) - 1)
        end = time.time()
        executionTimeDeterministic[dist].append(end - start)
        print(
            "Execution time of deterministic sort for "
            + dist
            + " array of size "
            + str(size)
            + " took "
            + str(end - start)
            + " seconds"
        )

        # Perform Randomized quick sort
        start = time.time()
        randomized_quicksort(data.copy(), 0, len(data) - 1)
        end = time.time()
        executionTimeRandomized[dist].append(end - start)
        print(
            "Execution time of randomized sort for "
            + dist
            + " array of size "
            + str(size)
            + " took "
            + str(end - start)
            + " seconds"
        )
        print("")

# Using matplot library to plot the graph of the execution time
plt.figure(figsize=(10, 6))
for dist in distributions:
    plt.plot(
        sizes,
        executionTimeDeterministic[dist],
        label=f"Deterministic - {dist}",
        linestyle="--",
    )
    plt.plot(
        sizes,
        executionTimeRandomized[dist],
        label=f"Randomized - {dist}",
        linestyle="-",
    )

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Deterministic vs Randomized Quicksort Performance")
plt.legend()
plt.grid()
plt.show()
