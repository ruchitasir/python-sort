# RADIX SORT
# Note: Input restricted to positive integers
# O(k*n) k: number of digits in largest number
# 3, 7, 17, 37, 127
def radix_sort(ls):
  # Determine k (length of largest num)
  k = len(str(max(ls)))
  # Start our k loop
  for i in range(k):
    # Make the 0-9 buckets
    buckets = make_buckets()
    # Make our n loop
    for j in range(len(ls)):
      # Determine the "place" we're looking at
      place = 10**i
      # Chop down the number to the correct digit
      digit = ls[j] // place
      # Get the bucket number
      bucket_num = digit % 10 # fit into the 10 buckets
      # Place the value into the correct bucket
      buckets[bucket_num].append(ls[j])
    # Mash the buckets back together
    ls = flatten(buckets)
  return ls

def flatten(buckets):
  flat = []
  for bucket in buckets:
    flat += bucket
  return flat

def make_buckets():
  buckets = []
  for i in range(10):
    buckets.append([])
  return buckets

# TEST DATA
test = [7, 3, 17, 37, 127, 333, 108, 999, 49, 521, 960, 187, 11, 16, 24, 48, 72, 360, 44, 676, 13, 42, 99, 101, 808, 206, 21, 22, 42, 10, 555, 15]
print('sorted list:', radix_sort(test))
# test1 = [7, 3, 17, 37, 127, 333, 108, 999, 49, 521, 960, 187, 11, 16, 24, 48, 72, 360, 44, 676, 13, 42, 99, 101, 808, 206, 21, 22, 42, 10, 555, 15]
# test2 = [960, 360, 10, 521, 11, 101, 21, 72, 42, 22, 42, 3, 333, 13, 24, 44, 555, 15, 16, 676, 206, 7, 17, 37, 127, 187, 108, 48, 808, 999, 49, 99]
# test3 = [101, 3, 206, 7, 808, 10, 11, 13, 15, 16, 17, 521, 21, 22, 24, 127, 333, 37, 42, 42, 44, 48, 49, 555, 960, 360, 72, 676, 187, 999, 99]
# test4 = [3, 7, 10, 11, 13, 15, 16, 17, 21, 22, 24, 37, 42, 42, 44, 48, 49, 72, 99, 101, 127, 187, 206, 333, 360, 521, 555, 676, 808, 960, 999]

# # Buckets:
# 0: []
# 1: []
# 2: []
# 3: []
# 4: []
# 5: []
# 6: []
# 7: []
# 8: []
# 9: []