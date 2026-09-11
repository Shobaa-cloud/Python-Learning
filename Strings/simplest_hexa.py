'''s = input()
ans = []
i = 0
while i < len(s):
    c = 1
    while i + c < len(s) and s[i] == s[i+c]:
        c += 1
    ans.append(s[i])
    ans.append(hex(c)[2:])
    i += c
print(''.join(ans)[::-1])'''
s = "aaaaaaaaaaabbbbbbbbbbbccccccccccc"

ans = []
c = 0

for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        c = 0

        for j in range(i, len(s)):
            if s[i] == s[j]:
                c += 1
            else:
                break

        ans.append(s[i])
        ans.append(hex(c)[2:])

print(''.join(ans)[::-1])