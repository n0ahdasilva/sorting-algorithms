'''
    PROJECT : Sorting Algorithms
    
    FILENAME : sorting_algorithms.py

    DESCRIPTION :
        Taking a look at different sorting algorithms and comparing how they work
        and their efficiency.
    
    FUNCTIONS :
        __init__()
        bubble_sort()
        bucket_sort()
        counting_sort()
        heap_sort()
            heapify()
        insertion_sort()
        merge_sort()
        quick_sort()
            partition()
        radix_sort()
            sort_digits()
        selection_sort()
        shell_sort()

    NOTES :
        Running into recursion limit errors on quick_sort() past 997 elements.
        
    AUTHOR :    Noah Arcand Da Silva    START DATE :    2021.08.22 (YYYY-MM-DD)

    CHANGES :
        1. Adding comments to explain time complexity.
        2. Adding new sorting algorithm fumctions.
    
    VERSION     DATE        WHO     DETAIL
    0.0.1b      2022.05.17  Noah    Adding new sorting algorithm functions.
'''

import math

class SortingAlgorithms:
    
    def __init__(self):

        self.item_list = [1, 2, 3]
        self._list_len = len(self.item_list)
    

    def __len__(self):

        return self._list_len
    
    # NOTE - Time Complexity:
    #           Best        O(n)
    #           Average     O(n^2)
    #           Worst       O(n^2)
    def bubble_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)

        for i in range(LIST_LENGTH):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True
            
            # Start looking at each item of the list one by one, comparing it with its 
            # adjacent value. With each iteration, the portion of the array that you 
            # look at shrinks because the remaining items have already been sorted.
            for j in range(LIST_LENGTH - i - 1):
                
                if nums_arr[j] > nums_arr[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    nums_arr[j], nums_arr[j + 1] = nums_arr[j + 1], nums_arr[j]
                    
                    # Since you had to swap two elements, set the `already_sorted` 
                    # flag to `False` so the algorithm doesn't finish prematurely
                    already_sorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                break
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best        O(n+k)
    #           Average     O(n)
    #           Worst       O(n^2)
    def bucket_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)
        DEFAULT_BUCKET_SIZE = 10
        # Determining the min and max values for
        # calculating the optimal number of buckets.
        min_value = int(min(nums_arr))
        max_value = int(max(nums_arr))

        buckets = []
        bucket_count = math.floor(((max_value - min_value) / DEFAULT_BUCKET_SIZE) + 1)
        # Create an array of size 'bucket_count'. Each slot of
        # this array is used as a bucket for storing elements.
        for i in range(bucket_count):
            buckets.append([])

        # Insert elements into the buckets from the array.
        # The elements are inserted according to the range of the bucket.
        for j in range(LIST_LENGTH):
            # Suppose, an input element is 63000 is taken, we negate the 
            # 'min_value' from it. It is then divided by 'bucket_size' = 10. 
            # Then, it is converted into an integer (ie. 18805.3≈18805). 
            bucket_index = math.floor((nums_arr[j] - min_value) / DEFAULT_BUCKET_SIZE)
            # Finally, 63000 is inserted into bucket-18805.
            buckets[bucket_index].append(nums_arr[j])
        
        # Sort individual buckets using selection_sort().
        for i in range(bucket_count):
            buckets[i] = self.selection_sort(buckets[i])

        # Concatenate the results together back into one list.
        k = 0
        for i in range(bucket_count):
            # Going through each slot of each bucket, and replacing nums_arr
            # with sorted values.
            for j in range(len(buckets[i])):
                nums_arr[k] = buckets[i][j]
                k += 1
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best        O(n+k)
    #           Average     O(n+k)
    #           Worst       O(n+k)
    def counting_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)

        # Initialize an array filled with 0's, with the 
        # same length as nums_arr.
        # NOTE: Both of these options work the same.
        output = [0] * LIST_LENGTH
        #output = [0 for i in range(LIST_LENGTH)]

        # Find out the range between min and max of the array.
        min_value = int(min(nums_arr))
        max_value = int(max(nums_arr))
        # Initialize an array of length max-min+1 with all elements 0. 
        # This array is used for storing the count of the elements in the array.
        count = [0] * (max_value - min_value + 1)
    
        # Store the count of each element at their respective 
        # index in 'count' array. (i.e. if 1 appears 3 times, count[1] will 
        # be 3. If 10 doesn't appear, count[10] = 0 ...)
        for i in range(0, LIST_LENGTH):
            # Since we have negative numbers, we are ofsetting the array 
            # by - min_value. (i.e. if min_value is -50, count[0] is position 
            # -50, count[50] is position 0, and count[100] is 50).
            count[nums_arr[i] - min_value] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this element in output array.

        # Store cummulative sum of the elements of the count array. It helps in 
        # placing the elements into the correct index of the sorted array.
        # (i.e. if 1 appears once, count[1] is 1, if 2 appears twice, count[2]
        # is 3 (2+1)).
        for i in range(1, len(count)):
            count[i] += count[i-1]
        # count[i] now contains actual position of this element in output array.
    
        # Build the output character array.
        # i = LIST_LENGTH - 1, while i >= 0:
        for i in range(LIST_LENGTH - 1, -1, -1):
            # Find the index of each element of the original array in the 
            # count array. This gives the cummulative count. Place the element 
            # at the index calculated. (i.e. if the cummulative sum of 4 is 6 in 
            # count[4], then 6-1=5 and 4 goes in output[5].)
            output[count[nums_arr[i] - min_value] - 1] = nums_arr[i]
            # We decrease the value of that index, so that if a number reappears
            # in our original array, we can place it appropriately.
            # (i.e. If 4 shows up again, it's cummulative sum is going to be 
            # 1 less in value, so 5-1=4 and 4 goes in output[4] instead of 
            # where it already appeared in output[5]).
            count[nums_arr[i] - min_value] -= 1
    
        # Copy the output array (sorted array) to nums_arr.
        for i in range(0, LIST_LENGTH):
            nums_arr[i] = output[i]
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best        O(n*log n)
    #           Average     O(n*log n)
    #           Worst       O(n*log n)
    def heap_sort(self, nums_arr):
       
        def heapify(nums_arr, n, i):
            # To maintain the max-heap property in a tree where both sub-trees are 
            # max-heaps, we need to run heapify on the root element repeatedly until it 
            # is larger than its children or it becomes a leaf node.
            
            # Find largest among root and children
            largest = i
            l = 2 * i + 1     # left = 2*i + 1
            r = 2 * i + 2     # right = 2*i + 2
        
            # See if left child of root exists and is greater than root
            if l < n and nums_arr[i] < nums_arr[l]:
                largest = l
            # See if right child of root exists and is greater than root
            if r < n and nums_arr[largest] < nums_arr[r]:
                largest = r
            # If root is not largest, swap with largest and continue heapifying
            if largest != i:
                nums_arr[i], nums_arr[largest] = nums_arr[largest], nums_arr[i]
                # To maintain the max-heap property for the entire tree, we will have to keep 
                # pushing downwards until it reaches its correct position.
                heapify(nums_arr, n, largest)

        # The main function to sort an array of given size LIST_LENGTH.

        LIST_LENGTH = len(nums_arr)

        # In the case of a complete tree, the first index of a non-leaf node 
        # is given by n/2 - 1. All other nodes after that are leaf-nodes and 
        # thus don't need to be heapified.
        for i in range(LIST_LENGTH//2 - 1, -1, -1): # for (int i = n / 2 - 1; i >=0; i--) {
            # We start by heapifying the lowest smallest trees 
            # and gradually move up until we reach the root element.
            heapify(nums_arr, LIST_LENGTH, i)

        # Since the tree satisfies Max-Heap property, 
        # then the largest item is stored at the root node.
        for i in range(LIST_LENGTH - 1, 0, -1):
            # Swap: Remove the root element and put at the end of the array (nth position). Put
            # the last item of the tree (heap) at the vacant place.
            nums_arr[i], nums_arr[0] = nums_arr[0], nums_arr[i]
            # Remove: Reduce the size of the heap by 1.
            # Heapify: Heapify the root element again so that we have the highest element at root.
            # # The process is repeated until all the items of the list are sorted.
            heapify(nums_arr, i, 0)
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best        O(n)
    #           Average     O(n^2)
    #           Worst       O(n^2)
    def insertion_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)

        for i in range(LIST_LENGTH):
            # Here 'current_num' will be compared with the previous elements.
            current_num = nums_arr[i]
            j = i - 1
            # Start looking at each item of the list one by one, 
            # comparing it with its previous value 'j'.
            while (j >= 0 and nums_arr[j] > current_num):
                # While the position of 'j' is bigger or equal to 0 (valid position the array)
                # and the previous value is still bigger to the current value, it will keep
                # swapping places with the previous value until it's in the right position.
                nums_arr[j], nums_arr[j + 1] = nums_arr[j + 1], nums_arr[j]
                # Adjust the position of the current value after the swap.
                j -= 1
            # Once the current number is in the correct position, it moves on
            # to the next number, and sets it as the 'current_num'.
            nums_arr[j + 1] = current_num
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best        O(n*log n)
    #           Average     O(n*log n)
    #           Worst       O(n*log n)
    def merge_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)
        # Makes sure the array is bigger than 1
        if LIST_LENGTH > 1:
            left_arr = nums_arr[:LIST_LENGTH//2]    # From the start of the array to the middle point.
            right_arr = nums_arr[LIST_LENGTH//2:]   # From the middle point of the array to the end.
            
            # Calling the merge_sort() algorithm recursively.
            self.merge_sort(left_arr)   # Sorting the first half.
            self.merge_sort(right_arr)  # Sorting the second half.

            i = 0   # Keep track of left most element in left_arr.
            j = 0   # Keep track fo left most element in right_arr.
            k = 0   # Merged array index.

            while i < len(left_arr) and j < len(right_arr):
                # If current value of left_arr is smaller than the current value
                # of right_arr, save value of left_arr in nums_arr[k].
                if left_arr[i] < right_arr[j]:
                    nums_arr[k] = left_arr[i]
                    i += 1  # Increment index of left_arr.
                # If current value of right_arr is smaller than the current
                # value of left_arr, save value of right_arr in nums_arr[k].
                else:
                    nums_arr[k] = right_arr[j]
                    j += 1  # Increment index of right_arr.
                k += 1  # Increment index of nums_arr.

            # If we viewed and transferred all of the right_arr, 
            # transfer the remainder of left_arr in nums_arr.
            while i < len(left_arr):
                nums_arr[k] = left_arr[i]
                i += 1
                k += 1
            # If we viewed and transferred all of the left_arr, 
            # transfer the remainder of right_arr in nums_arr.
            while j < len(right_arr):
                nums_arr[k] = right_arr[j]
                j += 1
                k += 1
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best	O(n*log n)
    #           Average	O(n*log n)
    #           Worst	O(n2)
    def quick_sort(self, nums_arr, low=None, high=None):
    # We set the default arguments as None for low and high, so the we don't have to enter
    # them when calling the function, and we can populate them with our function.
        
        def partition(nums_arr, low, high):
            # Choose the rightmost element as pivot (could be any element, in theory).
            pivot = nums_arr[high]
            # Pointer for greater element.
            i = low - 1
            # Traverse through all elements, and compare each element with pivot.
            for j in range(low, high):
                if nums_arr[j] <= pivot:
                    # If element smaller than pivot is found, swap it 
                    # with the greater element pointed by i.
                    i = i + 1
                    # Swapping element at i with element at j.
                    (nums_arr[i], nums_arr[j]) = (nums_arr[j], nums_arr[i])
            # Swap the pivot element with the greater element specified by i.
            (nums_arr[i + 1], nums_arr[high]) = (nums_arr[high], nums_arr[i + 1])
            # Return the position from where partition is done.
            return i + 1

        # The main function to sort an array of given size LIST_LENGTH.

        LIST_LENGTH = len(nums_arr)
        # Initializing our empty variables (usually only used for the first call).
        if low == None:
            low = 0
        if high == None:
            high = LIST_LENGTH - 1

        if low < high:
            # Find pivot element such that:
            # - element smaller than pivot are on the left.
            # - element greater than pivot are on the right.
            pi = partition(nums_arr, low, high)
            # Recursive call on the left of pivot.
            self.quick_sort(nums_arr, low, pi - 1)
            # Recursive call on the right of pivot.
            self.quick_sort(nums_arr, pi + 1, high)
        # Returns the sorted list of numbers.
        return nums_arr


    # NOTE - Time Complexity:
    #           Best	O(n+k)
    #           Average	O(n+k)
    #           Worst	O(n+k)
    def radix_sort(self, nums_arr):

        # Using modified counting sort to sort elements in the basis of significant places.
        def sort_digits(nums_arr, place):
            
            LIST_LENGTH = len(nums_arr)
            output = [0] * LIST_LENGTH
            count = [0] * 10

            # Calculate count of elements
            for i in range(0, LIST_LENGTH):
                index = nums_arr[i] // place
                count[index % 10] += 1

            # Calculate cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Place the elements in sorted order
            i = LIST_LENGTH - 1
            while i >= 0:
                index = nums_arr[i] // place
                output[count[index % 10] - 1] = nums_arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, LIST_LENGTH):
                nums_arr[i] = output[i]  

        # The main function to sort an array of given size LIST_LENGTH.
        
        # Get maximum element
        max_element = max(nums_arr)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            sort_digits(nums_arr, place)
            place *= 10       
        
        return nums_arr

    # NOTE - Time Complexity:
    #           Best	O(n^2)
    #           Average	O(n^2)
    #           Worst	O(n^2)
    def selection_sort(self, nums_arr):

        LIST_LENGTH = len(nums_arr)
        
        for step in range(LIST_LENGTH):
            min_idx = step

            for i in range(step + 1, LIST_LENGTH):
                
                # To sort in descending order, change > to < in this line
                # select the minimum element in each loop.
                if nums_arr[i] < nums_arr[min_idx]:
                    min_idx = i
                
            # Put min at the correct position.
            (nums_arr[step], nums_arr[min_idx]) = (nums_arr[min_idx], nums_arr[step])

        return nums_arr

    # NOTE - Time Complexity:
    #           Best	O(n*log n)
    #           Average	O(n^log n)
    #           Worst	O(n^2)
    def shell_sort(self, nums_arr):
        
        LIST_LENGTH = len(nums_arr)

        # Rearrange elements at each n/2, n/4, n/8, ... intervals
        interval = LIST_LENGTH // 2
        while interval > 0:
            for i in range(interval, LIST_LENGTH):
                temp = nums_arr[i]
                j = i
                while j >= interval and nums_arr[j - interval] > temp:
                    nums_arr[j] = nums_arr[j - interval]
                    j -= interval

                nums_arr[j] = temp
            interval //= 2

        return nums_arr