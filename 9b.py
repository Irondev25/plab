import re
import os

path = "/home/irondev25/Desktop/python/python_lab/"

dic = {}

for r,d,f in os.walk("."):
    for file in f:
        if(re.search(r"\.",file) is None):
            continue
        filex = re.split(r"\.", file)
        fname = filex[0]
        if(len(filex)>1):
            ext = filex[1]
        else:
            ext = "next"
        if(ext in dic.keys()):
            dic[ext].append(file)
        else:
            dic[ext] = list()
            dic[ext].append(file)


for key in dic.keys():
    print(key+":")
    for file in dic[key]:
        print(file)
    print("\n\n")

