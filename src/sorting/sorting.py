# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    # Your code here
    left_index, right_index = 0, 0
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index += 1
        else:
            merged_arr.append(arrB[right_index])
            right_index += 1

    merged_arr += arrA[left_index:]
    merged_arr += arrB[right_index:]
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
