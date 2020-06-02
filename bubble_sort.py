arr = [5,3,10,5,8,9,2,12]

arr1 = [500,30,10,65,24,90,32,120]

def bubble_sort(arr):
    length = len(arr)
   
    for j in range(length-1):
      status = False    
      for i in range(length-j-1):
         if arr[i] > arr[i+1]:
             temp = arr[i+1]
             arr[i+1] = arr[i]
             arr[i] = temp
             status = True
      if status == False: break
    return arr  

sorted_arr = bubble_sort(arr)
print(sorted_arr)

sorted_arr = bubble_sort(arr1)
print(sorted_arr)


# BUBBLE SORT
# O(n) best case, O(n^2) worst case
def bubble_sort_v(arr):
  # Loop through each element in the array
  for i in range(len(arr)):
    # Track whether anything has been swapped this round
    swapped = False
    for j in range(len(arr) - i - 1):
      # if it needs a swap, swap it
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j] # shortcut for swaps
        swapped = True
    # If you can break out early, do it
    if not swapped: break
  return arr