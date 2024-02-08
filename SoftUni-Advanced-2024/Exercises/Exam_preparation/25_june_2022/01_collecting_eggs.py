from collections import deque

egg_size = deque([int(x) for x in input().split(",")])
paper_size = deque([int(x) for x in input().split(",")])

BOX = 50
filled_boxes = 0

while egg_size and paper_size:
    egg = egg_size.popleft()
    paper = paper_size.pop()

    if egg <= 0:
        paper_size.append(paper)
        continue

    if egg == 13:
        first_paper = paper_size.popleft()
        paper_size.append(first_paper)
        paper_size.appendleft(paper)
        continue

    wrapped_egg = egg + paper
    if wrapped_egg <= BOX:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f'Eggs left: {", ".join(str(x) for x in egg_size)}')
if paper_size:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper_size)}')
