import string


def insertion(words) -> set:
    return {''.join((word[:i], char, word[i:])) for word in words
            for i in range(len(word)+1) for char in string.ascii_lowercase}


def deletion(words):
    return {''.join((word[:i], word[i+1:])) for word in words
            if len(word) > 1 for i in range(len(word))}


def substitution(words):
    return {''.join((word[:i], char, word[i+1:])) for word in words
            for i in range(len(word)) for char in string.ascii_lowercase}


def transposition(words):
    return {''.join((word[:i], word[i+1], word[i], word[i+2:]))
            for word in words for i in range(len(word)-1)}


def get_permutations(word, edit_dist):
    permutations = {word}

    for edit in range(edit_dist):
        permutations = (insertion(permutations) | deletion(permutations) |
                        substitution(permutations) | transposition(permutations))

    return permutations
