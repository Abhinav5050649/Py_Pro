'''
--> Program to practice basic file handling
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

def main():
    print(file_len("new.txt"))

main()'''

#Program to print all file in a directory having a specific extension
import os, glob

os.chdir("CPP")
for file in glob.glob("*.cpp"):
    print(file)


