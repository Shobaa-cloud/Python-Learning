# Question:
# Print a hollow diamond pattern for the given value of n.
#
# Example:
# Input: 4
#
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
#
# Approach:
# 1. Print the upper half of the diamond.
# 2. q is used to control the left-side spaces.
# 3. v and g are used to control the spaces between the two stars.
# 4. Print the lower half separately.
# 5. g is reduced by 2 in the lower half to decrease the inner spacing.
#
# Mistakes:
# - Initially the spacing logic for the lower half was different for
#   even and odd values of n, which caused hidden test failures.
# - Changed the spacing logic so that the same pattern works for
#   different values of n.
#
# What I learned:
# - How to print a hollow diamond using nested loops.
# - How to control spaces before and between stars.
# - How end="" helps print characters on the same line.
# - How changing the range value changes the number of spaces printed.


n=int(input())
v=0
q=n
for i in range(n):
    g=0
    for j in range(q-1):
        print(" ",end="")
    q-=1
    for k in range(1):
        print("*",end="")
    for l in range(v+i-1):
        print(" ",end="")
        g=g+1
    v+=1
    for f in range(1):
        if i==0:
            continue
        else:
            print("*",end=" ")
    print()
g=g-2
for i in range(n-1):
    for f in range(i+1):
        print(" ",end="")
    for j in range(1):
        print("*",end="")
    for b in range(g):
        print(" ",end="")
    g-=2
    for l in range(1):
        if i==n-2:
            continue
        else:
            print("*",end=" ")
    print()