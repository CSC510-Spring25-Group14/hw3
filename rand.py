"""
    This module generates 20 random elements in an array
"""
import random

def random_array(arr):
    """
        This function generates the random array using python built-in module random
    """
    shuffled_num = None
    for i in enumerate(arr):
        shuffled_num = random.randint(1, 20)
        arr[i[0]] = shuffled_num
    return arr
