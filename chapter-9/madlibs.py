import re
import os
from pathlib import Path
k=0
file = open(Path.cwd()/Path('temp.txt'))
text = file.read()
file.close()
regex = re.compile(r'(ADJECTIVE) or (NOUN) or (VERB)')
while k==0:
    part = regex.search(text)
    try:
        print(f"Enter a {part.group()}")
    except AttributeError:
        break
    subst = input()
    text = regex.sub(subst, text, 1)
print(text)
file = open(Path.cwd()/Path('temp2.txt'), 'w')
file.write(text)
file.close()