"""
This module implements quick sort and merge sort
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


# Quick sort function

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

merge_sort_arr = rand.random_array([None] * 20)
arr_out = merge_sort(merge_sort_arr)
print(arr_out)

quick_sort_arr = rand.random_array([None] * 20)
quick_sort(quick_sort_arr, 0, len(quick_sort_arr) - 1)
print("Sorted array using quick sort is:")
print(quick_sort_arr)
