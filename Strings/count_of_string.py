# Count the frequency of each word in a sentence

s = input().split()
b = []

for i in range(len(s)):
    if s[i] not in b:
        b.append(s[i])
        print(s[i], s.count(s[i]))