import string


def insertion(iterable) -> set:
    return {''.join((word[:i], char, word[i:])) for word in iterable
            for i in range(len(word)+1) for char in string.ascii_lowercase}


def deletion(iterable) -> set:
    return {''.join((word[:i], word[i+1:])) for word in iterable
            if len(word) > 1 for i in range(len(word))}


def substitution(iterable) -> set:
    return {''.join((word[:i], char, word[i+1:])) for word in iterable
            for i in range(len(word)) for char in string.ascii_lowercase}


def transposition(iterable) -> set:
    return {''.join((word[:i], word[i+1], word[i], word[i+2:]))
            for word in iterable for i in range(len(word)-1)}


def get_permutations(word, edit_dist) -> set:
    perms = {word}

    for edit in range(edit_dist):
        perms = (insertion(perms) | deletion(perms) | substitution(perms) |
                 transposition(perms))

    return perms
