# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 7, 0, len(arr) - 1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    if arr[0] < arr[len(arr)-1]:
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
        return -1

    elif arr[0] > arr[len(arr) - 1]:
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                end = mid - 1
            elif arr[mid] > target:
                start = mid + 1
        return -1
