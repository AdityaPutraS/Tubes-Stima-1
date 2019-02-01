import sys
import time
import random
from scorer import score
from solver import *

def main():
    ## SETUP
    # Getting file name from argv
    try:
        in_name = sys.argv[1]
        out_name = sys.argv[2]
    except IndexError:
        print("**[ERROR]** : Program parameter is incomplete")
        return 0
    
    # opening files
    try:
        inFile = open(in_name, "r+")
        outFile = open(out_name, "w")
    except FileNotFoundError:
        print("**[ERROR]** : Can't found specified file(s) path")
        return 0

    # Initializing a list to contain all test case
    test_case = [[int(x) for x in line.split()] for line in inFile.readlines()]

    # If inFile is empty create a new test case
    if len(test_case) == 0:
        deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        for i in range(0, 13):
            for j in range(0, 4):
                while True:
                    num = random.randint(1, 13)
                    if deck[num-1] > 0:
                        inFile.write(str(num) + " ")
                        break
            
            inFile.write("\n")
        # Resetting file object index to 0
        inFile.seek(0)

        # Reading file again
        test_case = [[int(x) for x in line.split()] for line in inFile.readlines()]

    ## MAIN CODE GOES HERE
    





    # Closing the file
    inFile.close()
    outFile.close()
    
main()