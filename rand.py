"""
    This code helps to generate an array of integers
"""
import random

def random_array(arr):
    """
        Input:
        arr (list)

        Returns:
            array of size len(arr) filled with random integers in the range [1, 20] (both inclusive)
    """
    for i in enumerate(arr):
        shuffled_num = random.randint(1, 20)
        arr[i[0]] = shuffled_num
    return arr
