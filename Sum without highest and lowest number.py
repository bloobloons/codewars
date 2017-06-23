# Sum all the numbers of the array except the highest and the lowest element (the value, not the index!).
#(The highest/lowest element is respectively only one element at each edge,
# even if there are more than one with the same value!)

#Example:
#{ 6, 2, 1, 8, 10 } => 16
#{ 1, 1, 11, 2, 3 } => 6

#If the array is empty, null or None, or if only 1 Element exists, return 0.

def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) < 3:
        return 0
    else:
        s = sorted(arr)
        chopped = s[1:-1]
        return sum(chopped)