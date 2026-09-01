# Question:
# Print the following pattern for a given n.
#
# Example for n = 3:
#
# 1
# 2 3
# 4 5 6
# 4 5 6
# 2 3
# 1
#
#
# Approach:
# 1. Store all the numbers printed in the first triangle inside a list.
# 2. Print the first triangle normally.
# 3. For the reverse triangle, start from the beginning of the required row.
# 4. Use len(a) - q to find the starting index of that row.
# 5. Print and remove each element from the list.
# 6. Since an element is removed, the next element automatically moves
#    into the same index.
#
#
# Mistakes:
# Initially I used:
#
# b = len(a) - 1 - i
#
# This pointed to the last element instead of the beginning of the row.
#
# Correct:
#
# b = len(a) - q
#
# This gives the starting position of the current row.
#
#
# What I learned:
# - len(a) gives the number of elements in a list.
# - a[b] accesses the element at index b.
# - a.remove(a[b]) removes that element from the list.
# - When an element is removed, the elements after it shift left.
# - The same index can therefore be used to print the next element.
# - end=" " prints values on the same line with a space.
# - q can be decreased using q -= 1.
#
#
# My solution:

n=int(input())
q=1
a=[]
r=n
for i in range(1,n+1):
    for j in range(i):
        print(q,end=" ")
        a.append(q)
        q=q+1
    print()
q=n
for i in range(1,n+1):
    b=len(a)-q
    for k in range(q):
        print(a[b],end=" ")
        a.remove(a[b])
    q-=1
    print()