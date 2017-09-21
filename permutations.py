import string


def insertion(iterable) -> set:
    """Returns up to 26*(n+1) insertions for each string in the iterable.

    :param iterable: Collection of strings to insert characters to.
    :return: A set of every insertion possible from the iterable.
    """
    return {''.join((word[:i], char, word[i:])) for word in iterable
            for i in range(len(word)+1) for char in string.ascii_lowercase}


def deletion(iterable) -> set:
    """Returns up to n deletions for each string in the iterable.

    :param iterable: Collection of strings to delete characters.
    :return: A set of every deletion possible from the iterable.
    """
    return {''.join((word[:i], word[i+1:])) for word in iterable
            if len(word) > 1 for i in range(len(word))}


def substitution(iterable) -> set:
    """Returns up to 26*n substitutions for each string in the iterable.

    :param iterable: Collection of strings to substitute characters.
    :return: A set of every substitution possible from the iterable.
    """
    return {''.join((word[:i], char, word[i+1:])) for word in iterable
            for i in range(len(word)) for char in string.ascii_lowercase}


def transposition(iterable) -> set:
    """Returns up to n-1 transpositions for each string in the iterable.

    :param iterable: Collection of strings to transpose characters.
    :return: A set of every transposition possible from the iterable.
    """
    return {''.join((word[:i], word[i+1], word[i], word[i+2:]))
            for word in iterable for i in range(len(word)-1)}


def get_permutations(word: str, edit_dist: int) -> set:
    """Returns every permutation for the string from the edit distance.

    :param word: String to perform insertions, deletions, substitutions, and
    transpositions on.
    :param edit_dist: Maximum number of changes that can be done on the word.
    :return: A set of every permutation of up to the given number of changes.
    """
    perms = {word}

    for edit in range(edit_dist):
        perms = (insertion(perms) | deletion(perms) | substitution(perms) |
                 transposition(perms))

    return perms
