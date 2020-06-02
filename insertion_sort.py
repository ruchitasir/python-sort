arr = [5,3,10,5,8,9,2,12]

arr1= [64, 25, 12, 22, 11]

arr2= [ 25, 12, 22, 11]

arr3= [ -25, 12, 22, -11]


def insertion_sort(arr):
    length = len(arr)
    for j in range(0,length-1): 
        j +=1  
        i = j 
        while i>0:
             if arr[i] < arr[i-1]:
                 temp = arr[i]
                 arr[i] = arr[i-1]
                 arr[i-1] = temp 
             i -= 1    
    return arr


arr = insertion_sort(arr3)
print(arr)    



# def insertion_sort(arr):
#     # marker = 0 
#     length = len(arr)
#     for j in range(0,length-1): # for j in range(1,length):
#         j +=1 #marker += 1  
#         i = j # marker
#         while i>0:
#              if arr[i] < arr[i-1]:
#                  temp = arr[i]
#                  arr[i] = arr[i-1]
#                  arr[i-1] = temp 
#              i -= 1    
#     return arr
      



# INSERTION SORT -- O(n^2)
# General idea is to start at the front of the list and
# go forward and sort each new element until we find the proper
# place to "insert". We'll call the front part "sorted" and the rest unsorted
def insertion_sort_v(ls):
    # Define the outer loop from 1 to the end of the list
    # Note: Use 1 and not 0 because we're doing a subtraction inside the loop
    for i in range(1, len(ls)):
        # Inside the outer loop, we will initialize a j variable set to i's value
        j = i
        # The inner loop will now count backward until we find the place we
        # want to insert at
        while j > 0:
            # If the value at j is greater than or equal to the value
            # to its left (j - 1), we done. Continue
            if ls[j] >= ls[j - 1]:
                break
            # Swap!
            ls[j], ls[j - 1] = ls[j - 1], ls[j]
            # Decrement j so we don't have an endless loop
            j -= 1
    # Remember to return the sorted list at the end!
    return ls