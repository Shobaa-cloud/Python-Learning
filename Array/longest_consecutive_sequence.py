# Question:
# Write a program to find the length of the longest consecutive
# elements sequence from a given unsorted array of integers.
#
# If two sequences have the same longest length, return 0.
#
# Example:
# Input: 49 1 3 200 2 4 70 5
# Output: 5
#
# Longest sequence: 1, 2, 3, 4, 5


# Approach:
# 1. For every element, check how many consecutive numbers follow it.
# 2. Store the length of each sequence in list 'a'.
# 3. Find the maximum sequence length.
# 4. Count how many times that maximum length occurs.
# 5. If it occurs more than once, print 0.
# 6. Otherwise, print the longest sequence length.


m=list(map(int,input().split()))
a=[]
f=0

for i in range(len(m)):
    b=1
    c=0

    for j in range(len(m)):
        if m[i]+b in m:
            c+=1
            b+=1

    a.append(c)

x=max(a)

for i in range(len(a)):
    if a[i]==x:
        f+=1

if f>1:
    print("0")
else:
    print(x+1)