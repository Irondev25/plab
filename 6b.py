import re
import os

pat = r".*\.mp3"
path = "/home/irondev25"

for r, d, f in os.walk(path):
    for file in f:
        if(re.search(pat, str(file)) is not None):
            print(file)

