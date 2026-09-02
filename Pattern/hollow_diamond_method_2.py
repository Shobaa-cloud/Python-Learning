# Hollow Diamond Pattern - Method 2
#
# Question:
# Print a hollow diamond pattern using stars (*).
#
# Approach:
# This is another method to print the hollow diamond.
# Instead of directly calculating the inner spaces,
# I used two variables:
# v -> controls the increasing inner space in the upper half
# c -> controls the decreasing inner space in the lower half
#
# The first loop prints the upper half of the diamond.
# The second loop prints the lower half.
#
# For the first and last rows of each half, the inside is empty.
# For the middle rows, spaces are printed inside to make it hollow.
#
# What I learned:
# - We can solve the same pattern problem using different logic.
# - Variables can be used as counters to control spaces.
# - range() can be used with changing values to increase/decrease spaces.
# - end="" helps print everything on the same line.
#
# Mistakes / Things I understood:
# - The number of inner spaces changes as we move towards
#   the middle and then decreases in the lower half.
# - The upper and lower halves need slightly different conditions.
#
# My Code:

n=int(input())
v=0
c=0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    print("*",end="")
    for k in range(v+i-1-1):
        if i==1:
            print("",end="")
        else:
            print(" ",end="")
            if i==n:
                c+=1
    v+=1
    if i==1:
        print("",end="")
    else:
        print("*",end="")
    print()

for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    print("*",end="")
    for k in range(0,c-1-1):
        print(" ",end="")
    c-=2
    if i==n-1:
        print("",end="")
    else:
        print("*",end="")
    print()