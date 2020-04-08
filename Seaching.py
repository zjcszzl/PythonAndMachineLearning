# Linear Search
def linearSearch(arr, target):
    for loc, val in enumerate(arr):
        if val == target:
            return loc
    return -1


# Binary Search
def binarySearch(arr, target):
    if len(arr) == 0:
        return -1
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    print(linearSearch([1, 2, 3, 46, 7, 8, 9, 2], 8))
    print(binarySearch([1, 3, 6, 9, 10, 24, 45, 78], 10))
    print("Done")
