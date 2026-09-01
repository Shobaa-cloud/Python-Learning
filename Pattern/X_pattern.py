# Question:
# Print an X star pattern for a given n.
#
# Example for n = 3:
#
# *   *
#  * *
#   *
#  * *
# *   *
#
#
# Approach:
# 1. Calculate the size of the square using:
#       a = 2*(n-1)+1
# 2. Use nested loops to go through every position.
# 3. Print "*" when the position lies on either diagonal.
# 4. Otherwise print a space.
#
#
# Mistakes:
# Initially I tried to control the two diagonals using separate variables
# and multiple loops.
#
# What I learned:
# - An X pattern can be created using two diagonal conditions.
# - i == j represents the main diagonal.
# - i + j == a-1 represents the opposite diagonal.
# - range(a) runs from 0 to a-1.
# - 2*(n-1)+1 gives the required odd size of the pattern.
#
#
# My solution:

n=int(input())
a=2*(n-1)+1

for i in range(a):
    for j in range(a):
        if i==j or i+j==a-1:
            print("*",end="")
        else:
            print(end=" ")
    print()