i = 1

try:
    while(1):
        print(i)
        i += 1
        if(i >= 20):
            raise StopIteration()
except StopIteration as e:
    print("caught exception")
