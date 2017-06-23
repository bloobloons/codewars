# Capitalise each word in a string input

import string

def toJadenCase(quote):
    if quote and not quote.isspace():
        return string.capwords(quote)