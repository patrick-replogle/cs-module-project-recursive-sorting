# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])

    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    while start <= mid and start2 <= end:
        if arr[start] > arr[start2]:
            temp = arr[start]
            index = start

            while index != start2:
                arr[index] = arr[index+1]
                index += 1

            arr[start2] = temp
        else:
            start += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)


arr = [5, 2, 3, 10, 9, 2]
merge_sort_in_place(arr, 0, 5)
print(arr)
