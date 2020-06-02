# QUICK SORT: best/average O(n*log(n)); worst O(n^2)
# BASE CASE(s): length of list less than or equal to 1
# RECURSIVE CASE: Any other length ----> 
        # 1. Pick a pivot element
        # 2. Divide into left and right, based on pivot
        # 3. Put it back together
            # a)   Quick sort the left
            # b) Quick sort the right
            # c) Concat left + pivot + right


def quick_sort(ls):
    # Check for base case
    if len(ls) <=1: return ls
    # 1. Pick a pivot element
    pivot = ls.pop() # pick the last element
    # 2. Divide into left and rigt, based on pivot
    left = [x for x in ls if x <= pivot] # list comprehension
    right = [x for x in ls if x > pivot]
    # 3. Put it back together
    return quick_sort(left) + [pivot] + quick_sort(right)


test = [2,1,5,2,6,9,1,5,4,3,7,5]
result = quick_sort(test)
print('result',result)
