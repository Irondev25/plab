def eval():
    x = int(input('Enter value of x'))
    if(x == 3 or x == -3):
        raise Exception("Invalid value of x")
    else:
        ans = 1.0/(9-pow(x, 2))
        print(ans)

try:
    eval()
except Exception as e:
    print("invalid input")
