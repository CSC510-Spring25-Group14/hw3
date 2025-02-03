"""
  This code contains implementation of few standard sorting algorithms
"""
import rand

def merge_sort(input_arr):
    """
        Input:
        arr (array of elements)

        Returns:
        arr in sorted order (sorted using merge sort algorithm)
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr)//2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))

def recombine(left_arr, right_arr):
    """
        Input:
        Two sorted arrays - left_arr, right_arr

        Returns:
        a single sorted array combining the elements of left_arr and right_arr
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

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

arr_for_insertion_sort = rand.random_array([None] * 20)
arr_for_insertion_sort_out = insertion_sort(arr_for_insertion_sort)

print(arr_for_insertion_sort_out)
