# Remove exclamation marks from the end of string (s)

def remove(s):

    if s == '':
        return s
    elif s[-1] == '!':
        return s[:-1]
    else:
        return s