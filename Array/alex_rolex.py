# Question:
# Find the minimum number of characters that must be deleted
# from two strings to make them equal.
#
# Example:
# Input:
# rolex
# alex
#
# Output:
# 3
#
# Explanation:
# rolex -> lex   (delete r, o)
# alex  -> lex   (delete a)
#
# Total deletions = 3


# My First Approach:
# I tried checking whether each character existed in the other
# string and counting the characters that were not present.
#
# This worked for simple cases like:
# rolex
# alex
#
# But it failed for cases where the same characters appeared
# in a different order or appeared multiple times.
#
# Example:
# abc
# cba
#
# Every character exists in both strings, but we cannot rearrange
# the characters. We can only delete them.

s1=input()
s2=input()

sl1=list(s1)
sl2=list(s2)

a=[]
b=[]

i=0
j=0

while i<len(sl1) and j<len(sl2):

    if sl1[i]==sl2[j]:
        a.append(sl1[i])
        i+=1
        j+=1

    else:
        if sl1[i] in sl2[j+1:]:
            b.append(sl2[j])
            j+=1
        else:
            b.append(sl1[i])
            i+=1

while i<len(sl1):
    b.append(sl1[i])
    i+=1

while j<len(sl2):
    b.append(sl2[j])
    j+=1

print(len(b))