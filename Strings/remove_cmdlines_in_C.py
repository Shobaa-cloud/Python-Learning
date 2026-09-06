# Question:
# Remove comments from a C program.
# Remove both // comments and /* */ comments.
# But do not remove /* */ when they appear inside a string.
# Also remove blank lines created by comments.


# Approach:
# 1. Read the complete input using sys.stdin.read()
# 2. Split the input into lines.
# 3. Check each character one by one.
# 4. Use inside_comment to know whether we are inside /* */.
# 5. Use inside_string to know whether we are inside " ".
# 6. If // is found, ignore the rest of that line.
# 7. If /* is found, ignore characters until */.
# 8. If /* */ occurs inside a string, keep it.
# 9. Store only lines containing actual code.
# 10. Join the remaining lines without extra blank lines.


# Mistakes:
# - Used chr(47) and chr(42) with lines instead of checking characters inside each line.
# - input() reads only one line, but this problem contains multiple lines.
# - Initially printed empty lines created after removing comments.
# - Thought comments inside ( ) should not be removed, but the important condition
#   is whether the comment-like text is inside a string.


# What I learned:
# - sys.stdin.read() reads the complete input, including multiple lines.
# - splitlines() separates a multiline string into individual lines.
# - "/" is the character used in // and /*.
# - "*" is used in /* and */.
# - A boolean variable can track whether we are currently inside a comment.
# - A boolean variable can track whether we are currently inside a string.
# - strip() removes spaces from the beginning and end while checking a line.
# - "\n".join() joins lines together using a newline.


import sys

n = sys.stdin.read()

lines = n.splitlines()

inside_comment = False
inside_string = False
output = []

for line in lines:
    result = ""
    j = 0

    while j < len(line):

        if inside_comment:
            if j + 1 < len(line) and line[j] == "*" and line[j + 1] == "/":
                inside_comment = False
                j += 2
            else:
                j += 1

        elif inside_string:
            result += line[j]

            if line[j] == '"':
                inside_string = False

            j += 1

        elif line[j] == '"':
            inside_string = True
            result += line[j]
            j += 1

        elif j + 1 < len(line) and line[j] == "/" and line[j + 1] == "*":
            inside_comment = True
            j += 2

        elif j + 1 < len(line) and line[j] == "/" and line[j + 1] == "/":
            break

        else:
            result += line[j]
            j += 1

    if result.strip() != "":
        output.append(result)

print("\n".join(output))