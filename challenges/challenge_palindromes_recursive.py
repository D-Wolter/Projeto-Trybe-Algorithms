def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False
    elif low_index >= high_index:
        return True
    elif not word[low_index] == word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
