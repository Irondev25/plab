import os

def walk_dir(path):
    for root,dirs,files in os.walk(path):
        print("files: ")
        for file in files:
            print(file)
        print("\nDirectory")
        for f in dirs:
            print(f)

walk_dir(".")
