import re

strings = re.findall(r"\d+\w*","This is a sample, 236dfg 56sdf isuhdngi")

for match in strings:
    print(match)