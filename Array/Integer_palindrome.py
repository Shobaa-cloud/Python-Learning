# Reverse and Add Until Palindrome
#
# Question:
# Take a number, reverse it and add it to itself.
# If the sum is not a palindrome, repeat the process
# until a palindrome is obtained.
#
# Example:
# 7325 + 5237 = 12562
# 12562 + 26521 = 39083
# 39083 + 39083 = 77166
# 77166 + 67177 = 144343
# 144343 + 343441 = 487784
#
# Approach:
# 1. Take the number as input.
# 2. Convert it into a string to reverse its digits.
# 3. Check if the original number is already a palindrome.
# 4. If it is not, repeatedly:
#    - Reverse the current number.
#    - Add it to the current number.
#    - Check whether the result is a palindrome.
# 5. Stop when a palindrome is obtained.
#
# What I learned:
# - A number can be reversed easily by converting it into a string
#   and using indexing with a step of -1.
# - int("".join(...)) can convert a reversed list of digits back
#   into an integer.
# - while loops are useful when the number of repetitions is unknown.
# - break can stop the loop as soon as the palindrome is found.
# - A number can be checked for palindrome by comparing it with
#   its reversed form.
#
# My Code:

n=int(input())
l=str(n)
a=[]
q=len(l)
b=n
ans=0

for i in range(q):
    c=b%10
    b=b//10
    a.append(c)
    q-=1

lit=int("".join(map(str,a)))

if n==lit:
    print("Given Number is already a palindrome")
    print(n,"is a palindrome")
else:
    while n>0:
        ans=n+lit
        al=[int(i) for i in str(ans)]
        ral=[]

        for k in range(len(al)-1,-1,-1):
            ral.append(al[k])

        if ral==al:
            print(int("".join(map(str,al))),"is a palindrome")
            break
        else:
            n=ans
            lit=int("".join(map(str,ral)))