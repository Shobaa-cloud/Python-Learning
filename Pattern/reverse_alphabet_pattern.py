    # Question:
# Write a program which displays the below pattern for a given value of n.
#
# Example:
# Input: 4
#
# J
# I H
# G F E
# D C B A
#
# Input: 3
#
# F
# E D
# C B A

# Mistake / What I didn't know:
# I didn't know how to print the pattern in reverse.
# I learned that a loop can be reversed using:
#
# range(start, stop, -1)
#
# But for this problem, instead of reversing the range,
# I used x -= 1 to move backwards through the alphabet.


# What I learned:
# 1. ASCII value of A is 65.
# 2. chr() converts an ASCII value into a character.
# 3. n*(n+1)//2 calculates 1+2+...+n.


n=int(input())
x=64+n*(n+1)//2

for i in range(1,n+1):
    for j in range(i):
        print(chr(x),end=" ")
        x-=1
    print()