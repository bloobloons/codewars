# our goal is to create a function that removes the first and last characters of a string. You're given one parameter.

def remove_char(s):
    if s != '':
        return s[1:-1]
    else:
        return s