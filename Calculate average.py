# Write function avg which calculates average of numbers in given list.

def find_average(array):
    if len(array) > 0:
        return (sum(array)/len(array))
    else:
        return 0