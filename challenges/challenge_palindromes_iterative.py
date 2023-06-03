def is_palindrome_iterative(word):
    if len(word) < 1:
        return False
    palavras = word.split()
    junto = ''.join(palavras)
    inverso = junto[::-1]
    if inverso == junto:
        return True
    else:
        return False
