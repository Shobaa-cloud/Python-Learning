# Cricket Scorecard - Find the score after one over
#
# Problem:
# Find the score after one over in a cricket match
# using the given cricket score card.
#
# . means no run
# Y means a WIDE (only bowler score gets added)
# Even number -> same batsman faces the next ball
# Odd number -> next batsman faces the next ball
# 6 balls per over
# Any other format -> Invalid
#
# Example:
# Input: 2461..
# Output:
# BATSMAN 1: 13
# BATSMAN 2: 0
# BOWLER: 13
#
# Input: 111111
# Output:
# BATSMAN 1: 3
# BATSMAN 2: 3
# BOWLER: 6
#
# Approach:
# - b1 stores Batsman 1's score
# - b2 stores Batsman 2's score
# - b stores the total bowler score
# - a and f are used to keep track of odd runs and decide which
#   batsman faces the next ball.
# - Even runs keep the same batsman.
# - Odd runs move the strike to the next batsman.
# - Y adds only 1 run to the bowler.
# - . adds no runs.
#
# Mistakes I made:
# - Initially I forgot to add numerical runs to the bowler score.
# - I used isalpha() to detect Y, which also accepts other letters
#   such as W, so invalid inputs were not detected correctly.
# - My first condition for deciding the batsman was incorrect,
#   especially for inputs like 111111.
#
# What I learned:
# - The bowler gets all runs, including batsman's runs.
# - A wide gives a run only to the bowler.
# - Even and odd runs determine who faces the next ball.
# - Conditions must carefully represent the actual state of the problem.
# - Testing with cases like 111111 helped me find a logic error
#   that was not obvious at first.


str = input()

b1, b2, b = 0, 0, 0
q = 1
a = 0
f = 0

for i in range(len(str)):
    c, d = 0, 0

    if str[i].isdigit() == True and f >= 0 and a <= f:
        c = int(str[i])

        b += c

        if c % 2 == 0:
            b1 += c
        else:
            b1 += c
            a += 1

    elif str[i].isdigit() == True and a >= 1:
        c = int(str[i])
        b += c

        if c % 2 == 0:
            b2 += c
        else:
            b2 += c
            f += 1

    elif str[i] == 'Y':
        b += 1

    elif str[i] == '.':
        b1 += 0
        b2 += 0
        b += 0

    else:
        print("Invalid")
        break

else:
    print("BATSMAN 1:", b1)
    print("BATSMAN 2:", b2)
    print("BOWLER:", b)