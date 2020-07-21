# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # iterate the array by creating a low pointer and a high pointer
     #find a base case
    if end >= start:
        # start = 0
        # end = len(arr) -1

        #get a middle index and retrieve the item with that index from list
        midd_point = (start + end) // 2
        guess = arr[midd_point]
       
        #if element is present at the middle
        if guess == target:
            return midd_point
        #if target is smaller than mid then it can only be present in left subarray
        if guess > target:
            return binary_search(arr, target, start, midd_point - 1)
        else:
            return binary_search(arr, target, midd_point + 1, end)

    else:
        #target is ot present in the array
        return -1
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, -4]
print(binary_search(arr, 9, 0, len(arr)))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass 
