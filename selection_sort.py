arr = [5,3,10,5,8,9,2,12]

arr1= [64, 25, 12, 22, 11]

arr2= [ 25, 12, 22, 11]

def selection_sort(arr):
        length = len(arr)
        # print('length',length)
        for j in range(length):
            min = arr[j]
            index =j
            for i in range(j, length):
                         if(min > arr[i]):
                                 min = arr[i]
                                 index = i
                            
            temp = arr[j]
            arr[j] = min
            arr[index] = temp
            print(arr)
        return arr    
            
selection_sort(arr1)



# def selection_sort(arr):
#         length = len(arr)
#         # print('length',length)
#         for j in range(length):
#             min = arr[j]
          
#             index =j
#             for i in range(j, length):
#                          print('min',min)   
#                          print('i',i) 
#                          print('arr i',arr[i])
#                          if(min > arr[i]):
#                                  min = arr[i]
#                                  index = i
#             print('min finally',min)
#             print('min index',index)
#             print('arr j',arr[j])                     
#             temp = arr[j]
#             arr[j] = min
#             arr[index] = temp
#             print(arr)
#         return arr  


# SELECTION SORT - O(n^2)
# This uses lowest index, but you can use highest instead
def selection_sort_v(arr):
    # Loop through n number of times
    for i in range(len(arr)):
        # lowest index starts at i - each iteration one more is "sorted"
        lowest_index = i
        # Loop through unsorted portion of the array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j
        # Swap the lowest into place
        arr[lowest_index], arr[i] = arr[i], arr[lowest_index]
    return arr
