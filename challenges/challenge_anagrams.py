def is_anagram(first_string, second_string):
    first = count_letters(first_string.lower())
    second = count_letters(second_string.lower())
    string1 = ordenar(first_string.lower())
    string2 = ordenar(second_string.lower())
    if first == second:
        if (string1 == '' or string2 == ''):
            res = (string1, string2, False)
            return res
        else:
            res = (string1, string2, True)
            return res
    else:
        res = (string1, string2, False)
        return res


def count_letters(string: str):
    total = {letter: 0 for letter in string}
    for letra in string:
        total[letra] = total[letra] + 1
    return total


def ordenar(string):
    if len(string) <= 1:
        return string
    base = string[0]
    equal = [c for c in string if c == base]
    before = [c for c in string if c < base]
    after = [c for c in string if c > base]

    return ordenar(''.join(before)) + ''.join(equal) + ordenar(''.join(after))
