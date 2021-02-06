# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    print("arrA", arrA)
    print("arrB", arrB)
    #merged_arr = [0] * num_elements - allocates all needed memory up front
    merged_arr = []

    # Starting at the beginning of "a" and "b"
    ind_a = 0
    ind_b = 0


    #compare the next value of each 
    while ind_a < len(arrA) and ind_b < len(arrB):
        print("ind_a ", ind_a)
        print("ind_b ", ind_b)
        if arrA[ind_a] < arrB[ind_b]:
            #add smallest to merged_arr
            merged_arr.append(arrA[ind_a])
            ind_a = ind_a + 1
        elif arrA[ind_a] == arrB[ind_b]:
            merged_arr.append(arrA[ind_a])
            merged_arr.append(arrB[ind_b])
            ind_a = ind_a + 1
            ind_b = ind_b + 1
        elif arrB[ind_b] < arrA[ind_a]:
            merged_arr.append(arrB[ind_b])
            ind_b = ind_b + 1

    #Loop to check if one of the arrays is longer
    while ind_a < len(arrA):
        merged_arr.append(arrA[ind_a])
        ind_a += 1

    while ind_b < len(arrB):
        merged_arr.append(arrB[ind_b])
        ind_b += 1

    print("print merged:", merged_arr)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    #Check the length of array

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]
    # recursively call merge_sort() on LHS
    new_left = merge_sort(lefthalf)
    #recursively call merge_sort() on RHS
    new_right = merge_sort(righthalf)
    #Merge sorted pieces
    return merge(new_left, new_right)

arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr2))

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

