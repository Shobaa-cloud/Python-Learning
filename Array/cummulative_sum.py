# PIN Array Decoder
# -----------------
# Problem:
# A PIN array contains numbers. For each number:
# 1. Find the cumulative sum of all its digits until a single digit is obtained.
# 2. Replace odd numbers with their respective lowercase alphabet.
#    1 = a, 2 = b, ..., 9 = i
# 3. Print the final six-digit PIN.

# Approach:
# - Read the numbers into a list.
# - If a number is already a single digit, add it directly.
# - Otherwise, calculate the sum of its digits.
# - If the sum is still greater than 9, repeat the process.
# - Store all final single-digit values.
# - Convert odd values into alphabets using chr().
# - Print everything together without spaces.

# What I learned:
# - str() can be used to separate the digits of a number.
# - List comprehension can convert those digits back into integers.
# - chr(96 + n) converts 1-9 into a-i.
# - extend() adds all elements of one list into another list.
# - sep="" prints elements without spaces.
# - Recursion can be used when the same operation needs to be repeated.

# Mistakes / Things I didn't know:
# - I initially didn't know about extend().
# - I didn't know that print(*list, sep="") could be used to print
#   the elements together without spaces.

n=int(input())
m=list(map(int,input().split()))

a=[]
d=[]

for i in range(n):
    if m[i]<10:
        a.append(m[i])
    else:
        def cs(p):
            t=0
            c=[]
            b=[int(i) for i in str(p)]
            for i in range(len(b)):
                t+=int(b[i])
            if t<10:
                c.append(t)
                a.extend(c)
            else:
                cs(t)

        cs(m[i])

for i in range(len(a)):
    if a[i]%2!=0:
        d.append(chr(96+a[i]))
    else:
        d.append(a[i])

print(*d,sep="")