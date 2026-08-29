# Take a string as input and print the first character that repeats.
#
# The character whose second occurrence appears first should be printed.
#
# Example 1:
# Input: banana
# Output: a
#
# Example 2:
# Input: abcdbea
# Output: b
#
# Example 3:
# Input: abcdef
# Output: No repeating element
#
# Rules:
# - No dictionary
# - No set()
# - Use basic string concepts, loops and conditions

n=input()
a=""
b=""
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if n[i]==n[j]:
            c+=1
    if n[i] not in a and c>=1:
        a+=n[i]
    else:
        b+=n[i]
if len(b)>1:
    print(b[0])
else:
    print("No repeating element")