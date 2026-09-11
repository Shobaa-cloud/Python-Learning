# Question:
# Given a string S, replace every substring of identical consecutive
# characters with the character followed by the hexadecimal
# representation of its count.
# Then reverse the resulting string.
#
# Example:
# Input:  aaaaaaaaaaa
# Count:  11
# Hex:    b
# Before reversing: ab
# After reversing:  ba
#
# Approach:
# 1. Find each group of consecutive identical characters.
# 2. Count how many times the character occurs consecutively.
# 3. Store the counts in a list.
# 4. Create a list containing count and character alternately.
# 5. Rearrange it as character + hexadecimal count.
# 6. Reverse the final string.
#
# Mistake I made:
# Initially, I was adding the count first and then the character
# while creating the final answer.
# But the required format is character + hexadecimal count.
#
# I also initially tried to move through the string using the count
# as the step in range(), which did not work because range() determines
# its steps before the count was updated.
#
# What I learned:
# - range() does not dynamically change its step value.
# - I should count only when a new consecutive group starts.
# - 11 in decimal is 'b' in hexadecimal.
# - The required format is LETTER + HEX COUNT.
# - The entire encoded string must be reversed at the end.
#
# My Code:

s="aaaaaaaaaaabbbbbbbbbbcccccccccccc"
c=1
a=[]
e=[]
fl=[]
ans=[]
for i in range(len(s)):
    if i==0 or s[i]!=s[i-1]:
        c=0
        for j in range(i,len(s)):
            if s[i]==s[j]:
                c+=1
            else:
                break
        a.append(c)
nl,al=0,0
for k in range(len(a)*2):
    if k%2==0 or k==0:
        e.append(a[nl])
        nl+=1
    else:
        e.append(s[al])
        al+=a[nl-1]
print(e)
for g in range(len(e)-2):
    if g%2!=0 and type(e[g])==str and e[g] not in fl:
        fl.append(e[g])
    else:
        if g%2==0 and type(e[g])==int and int(e[g+2])<int(e[g]):
            fl.append(e[g])
        else:
            break
for f in range(0,len(e),2):
    ans.append(e[f+1])
    ans.append(hex(e[f])[2:])
print(''.join(ans)[::-1])