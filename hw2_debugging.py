"""
This module implements quick sort and merge sort and insertion sort
"""
import rand

def merge_sort(arr):
    """
        This function implements merge sort of the two arrays
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """
        This function combines two arrays element-wise (ascending order)
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]
    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr

# Insertion Sort algorithm
# Added by mpartha

def insertion_sort(input_arr):
    """
        Input:
        arr (array of elements)

        Returns:
        arr in sorted order 
    """
    for i in range(len(input_arr)):
        j = i
        while j > 0 and input_arr[j - 1] > input_arr[j]:
            temp = input_arr[j - 1]
            input_arr[j - 1] = input_arr[j]
            input_arr[j] = temp
            j = j - 1
    return input_arr

def quick_sort(arr, low, high):
    """
        This function merges two partitioned arrays
    """
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    """
        This function partitions an array based on a pivot element
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

quick_sort_arr = rand.random_array([None] * 20)
quick_sort(quick_sort_arr, 0, len(quick_sort_arr) - 1)
print("Sorted array using quick sort is:")
print(quick_sort_arr)

def merge_sort_test_cases():
    """
        Test cases for merge sort function
    """
    arr_1 = [4, 5, 1, 6, 2, 8, 3]
    assert merge_sort(arr_1) == [1, 2, 3, 4, 5, 6, 8]

    arr_2 = [100, -50, 0, -2, 3, 87]
    assert merge_sort(arr_2) == [-50, -2, 0, 3, 87, 100]

    arr_3 = [9, 8, 5, -5, 0, -1]
    assert merge_sort(arr_3) == [-5, -1, 0, 5, 8, 9]
