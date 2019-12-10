import sys

args = {}
cmd_args = sys.argv

for i in range(1,len(sys.argv),2):
    args[cmd_args[i]]=cmd_args[i+1]

for key in args.keys():
    print(key+" "+args[key])