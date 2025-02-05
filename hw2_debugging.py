"""
Module for sorting algorithms with debugging improvements.
"""

import rand  # Ensure rand.py has the function random_array()

def merge_sort(input_arr):
    """Sorts an array using the merge sort algorithm."""
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2
    return merge(
        merge_sort(input_arr[:half]),
        merge_sort(input_arr[half:])
    )

def merge(left_arr, right_arr):
    """Merges two sorted arrays into one sorted array."""
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged.append(right_arr[right_idx])
            right_idx += 1

    merged.extend(left_arr[left_idx:])
    merged.extend(right_arr[right_idx:])
    return merged

def bubble_sort(input_array):
    """Sorts an array using the bubble sort algorithm."""
    arr_copy = input_array.copy()
    n = len(arr_copy)
    for i in range(n):
        swapped = False
        for j, _ in enumerate(arr_copy[:-1 - i]):  # Using enumerate for cleaner iteration
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy

# Generate a test array
TEST_ARRAY = rand.random_array(20)

# Sort using merge sort and bubble sort
sorted_merge = merge_sort(TEST_ARRAY)
sorted_bubble = bubble_sort(TEST_ARRAY)

# Print results
print(f"Merge sort result: {sorted_merge}")
print(f"Bubble sort result: {sorted_bubble}")
