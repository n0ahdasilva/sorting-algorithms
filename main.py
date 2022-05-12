'''
    PROJECT : Sorting Algorithms
    
    FILENAME : main.py

    DESCRIPTION :
        Taking a look at different sorting algorithms and comparing how they work
        and their efficiency.
    
    FUNCTIONS :
        rand_nums_gen()
        main()

    NOTES :
        Running into recursion limit errors on quick_sort() past 997 elements.
        
    AUTHOR :    Noah Arcand Da Silva    START DATE :    2021.08.22 (YYYY-MM-DD)

    CHANGES :
        1. Adding comments to explain time complexity.
        2. Adding new sorting algorithm fumctions.
    
    VERSION     DATE        WHO     DETAIL
    0.0.1b      2022.05.12  Noah    Adding new sorting algorithm functions.
'''

import secrets
import time

from sorting_algorithms import *

s = SortingAlgorithms()

def rand_nums_gen(ARRAY_LENGTH):

    rand_nums = []

    for i in range(ARRAY_LENGTH):  # Returns i numbers between a (included) and b (not included)
        rand_nums.append(secrets.SystemRandom().randrange(0, 500000))

    return rand_nums


def main():

    ARRAY_LENGTH = 10000
    SIG_FIG = 5

    NUM_ARR = rand_nums_gen(ARRAY_LENGTH)

    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.bubble_sort(arr_to_sort)  # Sort the array using bubble sort.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using bubble_sort().')

    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.bucket_sort(arr_to_sort) # Sort the array using bucket sort with insertion_sort() per bucket.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using bucket_sort() w/ insertion_sort() per bucket.')

    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.counting_sort(arr_to_sort)    # Sort the array using counting sort.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using counting_sort().')

    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.heap_sort(arr_to_sort)    # Sort the array using heap sort.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using heap_sort().')

    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.insertion_sort(arr_to_sort)   # Sort the array using insertion sort.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using insertion_sort().')
    
    arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
    start_time = time.process_time()    # Start timer for the sorting algorithm.
    s.merge_sort(arr_to_sort)   # Sort the array using merge sort.
    end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
    print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using merge_sort().')

    if len(NUM_ARR) < 998:    # If the array is too large to sort using quick sort, skip it. (Recursion limit error)
        
        arr_to_sort = NUM_ARR   # Ensure that the original array is not modified for fair comparison.
        start_time = time.process_time()    # Start timer for the sorting algorithm.
        s.quick_sort(arr_to_sort)   # Sort the array using quick sort.
        end_time = (time.process_time() - start_time)   # Stop timer after the array is sorted.
        print(ARRAY_LENGTH, 'numbers sorted in', round(end_time, SIG_FIG), 'using quick_sort().')
    
    else:
        print('Skipping quick_sort() because the array is too large. Will cause recursion limit error.')

if __name__ == "__main__":  # File is being run directly.
    main()