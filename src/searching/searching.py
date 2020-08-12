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
print(binary_search(arr, 1, 0, len(arr) - 1))


def descending_binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return descending_binary_search(arr, target, start, mid - 1)
    elif arr[mid] > target:
        return descending_binary_search(arr, target, mid + 1, end)


arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(descending_binary_search(arr2, 6, 0, len(arr) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    if arr[0] < arr[len(arr)-1]:
        return binary_search(arr, target, 0, len(arr) - 1)

    elif arr[0] > arr[len(arr) - 1]:
        return descending_binary_search(arr, target, 0, len(arr) - 1)


ascending = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
descending = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(agnostic_binary_search(ascending, 4))
print(agnostic_binary_search(descending, 6))
