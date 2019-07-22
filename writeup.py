#!/usr/bin/env python3

import os

readme = './readme.md'
html = './index.html'
path = './'
files = []

for r, d, f in os.walk(path):
    for file in f:
        if 'writeup.md' in file:
            files.append(os.path.join(r, file))


with open(readme, 'w') as f:
    print('# CTF writeups', file=f)
    print('', file=f)

    for x in files:
        print('- [{}]({})'.format( ' | '.join(x.split('/')[1:-1]), x), file=f)
