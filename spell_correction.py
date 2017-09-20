import permutations
import re
from collections import Counter


def best_fit(dict_path, test_path, sample_path, output_path,
             dict_encoding=None, test_encoding=None, sample_encoding=None,
             output_encoding=None, edit_dist=1):
    with open(dict_path, 'r', encoding=dict_encoding) as dict_file,\
            open(test_path, 'r', encoding=test_encoding) as test_file,\
            open(sample_path, 'r', encoding=sample_encoding) as sample_file,\
            open(output_path, 'w', encoding=output_encoding) as output:
        dictionary = {word.lower() for word
                      in filter(None, dict_file.read().splitlines())}
        test = [word.lower() for line in test_file.read().splitlines()
                for word in filter(None, re.split("[^A-Za-z']", line))]
        sample = Counter(word.lower() for line in sample_file.read().splitlines()
                         for word in filter(None, re.split("[^A-Za-z']", line)))

        for item in test:
            perms = permutations.get_permutations(item, edit_dist)
            include_apostrophes(perms)

            words = sorted([(word, sample[word]) if word in sample
                            else (word, 0) for word
                            in [perm for perm in perms if perm in dictionary]])

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
    # d = input('Enter dictionary file path: ')
    # t = input('Enter test file path: ')
    # s = input('Enter sample file path: ')
    best_fit('sample/dictionary.txt', 'sample/test.txt', 'sample/sample.txt',
             'sample/output.txt', sample_encoding='utf8')
