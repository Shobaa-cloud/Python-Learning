"""
QUESTION:
Find the highest frequency word in a given sentence.

EXAMPLE 1:
Input:
Way to Way. I said Way to go!

Output:
Way

EXAMPLE 2:
Input:
Return to the base. Right now. Return

Output:
Return

EXAMPLE 3:
Input:
What is this?

Output:
None


MY APPROACH:
1. Split the sentence into individual words.
2. Remove punctuation from each word.
3. Use nested loops to count how many times each word occurs.
4. Store the frequency of every word in a list.
5. Find the highest frequency.
6. Find the position of that highest frequency.
7. If the highest frequency is greater than 1, print the word.
8. Otherwise, print None.


MISTAKES / EDGE CASES:
- Punctuation such as '.', '!', '?' can be attached to words.
- strip() must be applied to each word, not the entire sentence.
- Calling input() more times than the provided input causes EOFError.
- Accessing an index that does not exist causes IndexError.
- If every word occurs only once, the answer should be None.
- max() can still return 1, so the frequency must be checked.


WHAT I LEARNED:
- split()
- strip()
- nested loops
- max()
- index()
- len()
- indexing
- conditional statements
- EOFError
- IndexError
- Strings and lists behave differently
"""


s = input().split()
for i in range(len(s)):
    s[i] = s[i].strip(".,!?")
a = []
for i in range(len(s)):
    c = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            c += 1
    a.append(c)
n = max(a)
m = a.index(n)
if max(a) > 1:
    print(s[m])
else:
    print("None")