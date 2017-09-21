import permutations
import re
from collections import Counter


def suggestions(string, dictionary, edit_dist=1):
    return [perm for perm in permutations.get_permutations(string, edit_dist)
            if perm in dictionary]


def best_fit(string, dictionary, sample, edit_dist=1):
    return max([(perm, sample[perm]) if perm in sample else (perm, 0)
                for perm in permutations.get_permutations(string, edit_dist)
                if perm in dictionary], key=lambda x: x[1])[0]


def sample_test(edit_dist=1):
    with open('sample/dictionary.txt', 'r') as dict_file,\
            open('sample/test.txt', 'r') as test_file,\
            open('sample/sample.txt', 'r', encoding='utf8') as sample_file,\
            open('sample/output.txt', 'w') as output:
        dictionary = {word.lower() for word
                      in filter(None, dict_file.read().splitlines())}
        test = [word.lower() for line in test_file.read().splitlines()
                for word in filter(None, re.split("[^A-Za-z']", line))]
        sample = Counter(word.lower() for line in sample_file.read().splitlines()
                         for word in filter(None, re.split("[^A-Za-z']", line)))

        for item in test:
            perms = permutations.get_permutations(item, edit_dist)
            include_apostrophes(perms)

            words = sorted([(perm, sample[perm]) if perm in sample
                            else (perm, 0) for perm in perms
                            if perm in dictionary])

            if item in dictionary:
                print(item.capitalize(), "is a real word.", file=output)
            print('Possible words for ', item, ': ', sep='', end='',
                  file=output)
            if words:
                print(', '.join([w for w,_ in words]), file=output)
                print('Suggested word:', max(words, key=lambda x: x[1])[0],
                      end='\n\n', file=output)
            else:
                print('No possible words found', end='\n\n', file=output)


def include_apostrophes(words):
    words.update({''.join((word[:len(word)-1], "'", word[len(word)-1]))
                  for word in words if word.endswith('s') and len(word) > 1})


if __name__ == '__main__':
    sample_test(edit_dist=1)
