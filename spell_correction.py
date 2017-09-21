import permutations
import re
from collections import Counter

while True:
    try:
        edit_dist = int(input("Enter edit distance (as an integer): "))
    except ValueError:
        continue
    else:
        break

with open('sample/dictionary.txt', 'r') as dict_file, \
        open('sample/test.txt', 'r') as test_file, \
        open('sample/sample.txt', 'r', encoding='utf8') as sample_file, \
        open('sample/output.txt', 'w') as output:
    dictionary = {word.lower() for word
                  in filter(None, dict_file.read().splitlines())}
    test = [word.lower() for line in test_file.read().splitlines()
            for word in filter(None, re.split("[^A-Za-z']", line))]
    sample = Counter(word.lower() for line in sample_file.read().splitlines()
                     for word in filter(None, re.split("[^A-Za-z']", line)))

    for item in test:
        perms = permutations.get_permutations(item, edit_dist)

        perms.update({''.join((perm[:len(perm)-1], "'", perm[len(perm)-1]))
                      for perm in perms
                      if perm.endswith('s') and len(perm) > 1})

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
