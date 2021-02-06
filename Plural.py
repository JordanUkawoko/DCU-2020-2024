#!/usr/bin/env python3

import sys


es_endings = ('ch', 'sh', 'x', 's', 'z', 'o')
ves_endings = ('fe', 'f')
vowels = 'aeiou'

def plural(noun):
    if noun.endswith(es_endings):
        return noun + 'es'

    if noun.endswith(ves_endings):
        [root, suffix] = noun.rsplit('f', 1)
        return root + 'ves'

    if noun[-1] == 'y' and noun[-2] not in vowels:
        return noun[: -1] + 'ies'

    return noun + 's'

def main():
    for line in sys.stdin:
        print(plural(line.strip()))

if __name__ == '__main__':
    main()
