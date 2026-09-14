# Coin Piles
#
# Problem:
# You have two coin piles containing a and b coins.
# In each move, you can either:
# 1. Remove 2 coins from the left pile and 1 from the right pile
# 2. Remove 1 coin from the left pile and 2 from the right pile
#
# Check whether both piles can be emptied.
#
# Approach:
# I used a while loop to repeatedly make a valid move.
# If the first pile has more coins, I remove 2 from it
# and 1 from the second pile.
# Otherwise, I remove 1 from the first pile
# and 2 from the second pile.
#
# The loop continues until one of the piles becomes 0.
# Then I check whether both piles became 0.
#
# Mistake I made:
# Initially, I used a while loop but never changed the values
# of a and b inside the loop.
# So the same condition was checked again and again,
# causing an infinite loop and Time Limit Exceeded.
#
# What I learned:
# In a while loop, the values involved in the condition
# must eventually change so that the loop can stop.


n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    while a != 0 and b != 0:

        if a > b:
            if a >= 2 and b >= 1:
                a = a - 2
                b = b - 1
            else:
                break

        else:
            if a >= 1 and b >= 2:
                a = a - 1
                b = b - 2
            else:
                break

    if a == 0 and b == 0:
        print("YES")
    else:
        print("NO")