import os,time

def child():
    for i in range(5):
        time.sleep(1)
        print(str(os.getpid())+" ->"+str(i+1))
    exit(0)

for i in range(5):
    n = os.fork()
    if(n>0):
        print("process("+str(n)+") spawned")
    else:
        child()

