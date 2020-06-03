from random import shuffle
tries = 0

def is_sorted(ls):
    # Loop through the list
    # Make sure each item is less than or equal to the next
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]: return False
    return True

def bogosort(ls):
    global tries
    tries +=1
    # Check if already sorted
    if is_sorted(ls): return ls
    # if not, shuffle list
    shuffle(ls)
    # And check again
    return bogosort(ls)

test = [9,2,8,1]

print('sorted list', bogosort(test), 'and we got it in',tries,'tries')