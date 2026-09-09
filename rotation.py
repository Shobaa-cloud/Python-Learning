# Question:
# Check whether two strings are rotations of each other.
#
# Example:
# Input:
# Hello
# elloH
#
# Output:
# Hello and elloH are rotation of each other


# My First Approach:
# I tried comparing the first and last characters of both strings
# and removing the matching characters.
#
# This worked for the given test cases but failed in hidden tests.
#
# Mistake:
# I only considered rotations involving the first and last characters.
# A string can be rotated from ANY position.
#
# Example:
# abcdef
# cdefab
#
# These are rotations, but my original logic could not detect them.


# Better Approach:
# If m is a rotation of n, then m will always appear inside n+n.
#
# Example:
# n = abcdef
# n+n = abcdefabcdef
#
# cdefab appears inside abcdefabcdef.
#
# So we can simply check:
# m in n+n


n=input()
m=input()

if len(n)==len(m) and m in n+n:
    print(n,"and",m,"are rotation of each other")
else:
    print("Not a rotation of each other")


# What I Learned:
# 1. A rotation can start from any position, not just the first or last.
# 2. Hidden test cases can expose assumptions in my logic.
# 3. Checking m in n+n is a simple way to detect string rotations.
# 4. Always think about different possible positions when solving problems.