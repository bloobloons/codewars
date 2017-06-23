# Write a function longest() that takes one argument, a list of words,
# and returns the length of the longest word in the list.

def longest(words):
    lengths = []

    for each in words:
        lengths.append(len(each))

    return max(lengths)
