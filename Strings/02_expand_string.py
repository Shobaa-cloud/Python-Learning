"""
QUESTION:
Expand the string based on the numbers given in between as given in the example.
The number will be a value between 1 to 20.

EXAMPLES:

Input:
He3m2o

Output:
Heeemmo

Input:
Tryme

Output:
Tryme

Input:
G20MA3

Output:
GGGGGGGGGGGGGGGGGGGGMAAA


MY APPROACH:
1. Take the input as a string.
2. Check the character after the current character.
3. If the next character is an alphabet, print the current character normally.
4. If the next character is a digit, check whether it is a one-digit or two-digit number.
5. Store the number and multiply the previous character by that number.
6. Handle the last character separately.


MISTAKES / EDGE CASES:
- n[i+2] can cause an IndexError when i is near the end.
- Added i+2 < len(n) before accessing n[i+2].
- Numbers can have one or two digits because the value is between 1 and 20.
- q must be reset after using it.
- The last character needs to be handled separately.
- Digits should not be printed separately.


WHAT I LEARNED:
- isalpha()
- isdigit()
- int()
- string multiplication
- indexing
- i+1 and i+2 look-ahead
- len()
- IndexError
- Handling one-digit and two-digit numbers
"""


n=input()
q=""
for i in range(len(n)-1):
    if n[i+1].isalpha():
        print(n[i] if n[i].isdigit()==False else "",end="")
    else:
        if i+2<len(n) and n[i+1].isdigit() == n[i+2].isdigit():
            q+=n[i+1]
            q+=n[i+2]
            print(n[i]*int(q),end="")
            q=""
        else:
            m=int(n[i+1])
            print(n[i]*m,end="")
print(n[-1] if n[-1].isalpha() else "",end="")