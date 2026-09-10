# Prefix-Suffix Matching
# Approach:
# 1. Store the input string as a list.
# 2. Remove the first character one by one to create different suffixes.
# 3. Compare each suffix with the beginning of the original string.
# 4. Count the matching characters until the first mismatch.
# 5. Print the total count.

n=int(input())

for i in range(n):
    t=0
    st=input().strip()
    s=list(st)
    c=len(s)
    a=[]

    a.extend(s)

    while len(a)>0:
        if len(a)>0:
            a.remove(a[0])
        else:
            break

        for k in range(len(a)):
            if a[k]==s[k]:
                c+=1
            else:
                break

    print(c)