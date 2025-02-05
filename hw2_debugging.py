import rand

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

def bubbleSort(arr):
    arr_copy = arr.copy()  
    for i in range(n):
        for j in range(n):  # Should be range(n - 1)
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)
bubble_out = bubbleSort(arr)  # This line will trigger an IndexError

print(arr_out)
