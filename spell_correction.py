import permutations
import re
from collections import Counter


def suggestions(string, edit_dist=1):
    """Returns a set of permutations that are in the dictionary.

    :param string: String to perform permutations on.
    :param edit_dist: Maximum number of changes that can be done on the word.
    :return: Every permutation of the string that is in the dictionary.
    """
    return {perm for perm in permutations.get_permutations(string, edit_dist)
            if perm in dictionary}


def with_apostrophe(string, edit_dist=1):
    """Returns a set of real permutations including ones with apostrophes.

    :param string: String to perform permutations on.
    :param edit_dist: Maximum number of changes that can be done on the word.
    :return: Every permutation that is available in the dictionary, including
    ones that end with 's, if within edit distance.
    """
    perms = permutations.get_permutations(string, edit_dist)
    perms.update({''.join((perm[:len(perm)-1], "'", perm[len(perm)-1]))
                  for perm in perms if perm.endswith('s') and len(perm) > 1})

    return {perm for perm in perms if perm in dictionary}


with open('sample/dictionary.txt', 'r') as dict_file:
    dictionary = {word.lower() for word
                  in filter(None, dict_file.read().splitlines())}

if __name__ == '__main__':
    while True:
        try:
            edit_dist = int(input('Enter the edit distance (integer): '))
        except ValueError:
            continue
        else:
            break

    with open('sample/test.txt', 'r') as test_file, \
            open('sample/sample.txt', 'r', encoding='utf8') as sample_file, \
            open('sample/output.txt', 'w') as output:
        test = [word.lower() for line in test_file.read().splitlines()
                for word in filter(None, re.split("[^A-Za-z']", line))]
        sample = Counter(word.lower() for line
                         in sample_file.read().splitlines() for word
                         in filter(None, re.split("[^A-Za-z']", line)))

        for item in test:
            if item in dictionary:
                continue

            words = sorted([(perm, sample[perm]) if perm in sample
                            else (perm, 0) for perm
                            in suggestions(item, edit_dist)])

            if words:
                print('Possible words for "', item, '": ', sep='', end='',
                      file=output)
                print(', '.join([w for w,_ in words]),
                      file=output)
                print('Suggested word:', max(words, key=lambda x: x[1])[0],
                      end='\n\n', file=output)
            else:
                print('No real words found for "', item, '".', sep='',
                      end='\n\n', file=output)
