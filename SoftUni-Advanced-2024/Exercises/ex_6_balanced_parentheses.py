from collections import deque
parentheses = deque(input())
open_parentheses = "{[("
close_parentheses = ")]}"
while parentheses:
    if parentheses[0] in close_parentheses:
        print("NO")
        break
    if parentheses[0] == open_parentheses[0] and parentheses[-1] == close_parentheses[2] \
            or parentheses[0] == open_parentheses[1] and parentheses[-1] == close_parentheses[1] \
            or parentheses[0] == open_parentheses[2] and parentheses[-1] == close_parentheses[0]:
        parentheses.popleft()
        parentheses.pop()
    else:
        print("NO")
        break
else:
    print("YES")
