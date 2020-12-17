'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import re

fileName = input()
reg = input()
inputFile = open(fileName, mode="r")
fileLines = inputFile.readlines()
for line in fileLines:
    if re.search(reg, line):
        print(line)