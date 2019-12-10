import random

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

# Function to check parentheses


def generate():
    n = random.randint(2,20)
    patt = ""
    for i in range(n):
        x = random.random()
        if(x > 0.5):
            patt+="["
        else:
            patt+="]"
    return patt


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


# Driver code
string = generate()
print(string, "-", check(string))

string = generate()
print(string, "-", check(string))
