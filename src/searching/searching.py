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
def agnostic_binary_search(arr, target):    # iterate the array by creating a low pointer and high pointer(last item in the list)
    low = 0
    high = len(arr) -1
    #create a loop that will continue while low is less than or equel to the hig pointer
    while low <= high:
        #get middle index
        midd_point = (low + high) // 2
        #retrieve the item with that index from list
        guess = arr[midd_point]
        #There are three options, correct, too high or too low
        if guess == target:
            return midd_point
        if arr[low] <= arr[high]: #ascending
            if guess > target:
                high = midd_point - 1

            else:
                low = midd_point + 1
        else:
            if target > arr[midd_point]: #descending
                high = midd_point -1 #target can be in first half
            else: #target > arr[middle]
                low = midd_point + 1 #target can be in second half


    return -1  # not found
    
ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
print(agnostic_binary_search(ascending, 14))
