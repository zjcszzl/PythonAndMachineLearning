# Bubble Sort
def bubbleSort(arr):
    if len(arr) <= 0:
        return
    for i in range(len(arr)-1):
        isSorted = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        if isSorted:
            break
    return arr


# Selection Sort
def selectionSort(arr):
    if len(arr) == 0:
        return
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Insertion Sort
def insertionSort(arr):
    if len(arr) == 0:
        return
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] >= temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


# Merge Sort
def mergeSort(arr):
    if len(arr) == 0:
        return
    elif len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    i, j = 0, 0
    cur = []
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                cur.append(left[i])
                i += 1
            else:
                cur.append(right[j])
                j += 1
        elif i < len(left):
            cur.append(left[i])
            i += 1
        elif j < len(right):
            cur.append(right[j])
            j += 1
    return cur


# Quick Sort
def quickSort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    def partition():
        pivot = arr[-1]
        boundary = -1
        for index in range(len(arr)):
            if arr[index] <= pivot:
                boundary += 1
                arr[boundary], arr[index] = arr[index], arr[boundary]
        return boundary

    loc = partition()
    return quickSort(arr[:loc]) + [arr[loc]] + quickSort(arr[loc+1:])


# Count Sort
def countSort(arr, K):
    count = [0] * (K+1)
    for val in arr:
        count[val] += 1
    i = 0
    for index in range(len(count)):
        while count[index] > 0:
            arr[i] = index
            count[index] -= 1
            i += 1
    return arr


# Bucket Sort
def bucketSort(arr, num):
    l = [[] for i in range(num)]
    for val in arr:
        l[val // num].append(val)
    for elem in l:
        elem.sort()
    res = []
    for elem in l:
        res += elem
    return res


if __name__ == "__main__":
    print(bubbleSort([3, 2, -1, 5, 3, 2, 5, 7]))
    print(selectionSort([-13, 2, -1, 5, 3, -9]))
    print(insertionSort([-13, -19, 2, 3, 4, 5, 5, 8, 1, 1, 1]))
    print(mergeSort([3, 2, -1, 5, 3, 2, 5, 7]))
    print(quickSort([3, 2, -1, -6, 7, 8, 4, 5, 3]))
    print(countSort([3, 2, 1, 3, 3, 3, 3, 3], 3))
    print(bucketSort([3, 2, 1, 6, 7, 8, 4, 5, 3], 4))
    print("Done")
