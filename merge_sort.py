#MERGE SORT- best/average O(n*log(n)); worst - O(n^2)
# def merge_sort(ls):
#     # Base case: 1 or fewer items is considered sorted
#     if len(ls)<=1:
#          return ls
#     # Recursive case : any other length
#     # 1. Find the mid-point of list 
#     mid = len(ls) // 2 # gives us an int and floor the number
#     # 2. Divide list in half  
#     left = ls[:mid]
#     right = ls[mid:]
#     # 3. Sort each side
#     left_sorted = merge_sort(left)
#     right_sorted = merge_sort(right)
#     # 4. Merge the two lists back together
#     return merge(left_sorted,right_sorted)

def merge_sort(ls):
    # Base case: 1 or fewer items is considered sorted
    if len(ls)<=1: return ls
    # Recursive case : any other length ,   
    # 1. Find the mid-point of list 
    # mid = len(ls) // 2 # gives us an int and floor the number
    # 2. Divide list in half  , # 3. Sort each side ,    # 4. Merge the two lists back together
    return merge(merge_sort(ls[:(len(ls) // 2)]),merge_sort(ls[(len(ls) // 2):]))


# O(n)- combines two sorted lists into one sorted list
def merge(ls1,ls2):
    marker1 = 0 
    marker2 = 0
    length = len(ls1)+len(ls2)
    ls =[]
    for i in range(length):
        if marker1 >= (len(ls1) ):
            ls.append(ls2[marker2])
            marker2 += 1
        elif marker2 >= (len(ls2)):    
            ls.append(ls1[marker1])
            marker1 += 1
        else:
             if ls1[marker1] >= ls2[marker2]:
                 ls.append(ls2[marker2])
                 marker2 += 1
             else: # when ls1[marker1] < ls2[marker2]:
                 ls.append(ls1[marker1])
                 marker1 += 1         
    print(ls)
    return ls    

merge_sort([4,2,1,8,7,9,5,3,7,3,5])

# def merge(ls1,ls2):
#     marker1 = 0 
#     marker2 = 0
#     length = len(ls1)+len(ls2)
#     ls =[]
#     for i in range(length):
#         print('marker1',marker1)
#         print('marker2',marker2)
#         if marker1 >= (len(ls1) ):
#             ls.append(ls2[marker2])
#             marker2 += 1
#         elif marker2 >= (len(ls2)):    
#             ls.append(ls1[marker1])
#             marker1 += 1
#         else:
              
#              if ls1[marker1] >= ls2[marker2]:
#                  ls.append(ls2[marker2])
#                  marker2 += 1
#              else: # when ls1[marker1] < ls2[marker2]:
#                  ls.append(ls1[marker1])
#                  marker1 += 1
#         print(ls)     
#     print(ls)
#     return ls   

# merge([2,4,12],[3,5,7,8,9])

# merge_sort([4,2,1,8,7,9,5,3,12])

# merge_sort([4,2,1,8,7,9,5,3,7,3,5])

