import re
import os

pat = r".*\.py"
path = "/home/irondev25/Desktop/python"

for r,d,f in os.walk("."):
    for file in f:
        if(re.search(pat,str(file)) is not None):
            print(file)
