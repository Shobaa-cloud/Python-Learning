# Minimum Number of Jumps
#
# Question:
# Given an array where each element represents the maximum
# number of steps that can be made forward from that element,
# find the minimum number of jumps needed to reach the end.
#
# Example:
# 1 4 3 2 6 7
#
# Start at position 0.
# l[0] = 1  -> jump to position 1
# l[1] = 4  -> jump to position 5 (last position)
#
# Answer = 2
#
# Approach:
# q represents the current position.
# b represents the maximum number of positions we can jump
# from the current position.
#
# q + b gives the position we can reach using the maximum jump.
# len(l)-1 gives the last index of the array.
#
# If q+b reaches or passes the last index, we count the jump
# and stop.
# Otherwise, we move q forward by b and continue.
#
# What I learned:
# - The value in the array represents jump distance.
# - q represents the current position.
# - b represents how far I can jump.
# - q+b represents the destination after the maximum jump.
# - len(l)-1 is the last index of the list.
# - break stops the loop when the end is reached.
#
# Mistakes I made:
# - I originally compared l[i] and l[i+1], but this problem
#   is not about comparing the values.
# - I used q+=b twice, which made q go outside the list.
# - I initially used > instead of >= when checking the last index.
#
# My Code:

n=int(input())
a=[]
c=0

for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    q=0

    while True:
        b=l[q]

        if q+b>=len(l)-1:
            c+=1
            break

        c+=1
        q+=b

    print(c)
    c=0