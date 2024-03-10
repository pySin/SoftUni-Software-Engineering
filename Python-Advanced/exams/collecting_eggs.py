# Collecting Eggs
from collections import deque


eggs = deque([int(e) for e in input().split(", ")])
papers = deque([int(p) for p in input().split(", ")])
BOX_SIZE = 50


boxes_count = 0
while eggs and papers:

    current_egg = eggs.popleft()
    current_paper = papers.pop()

    if current_egg == 13:
        first_paper = papers.popleft()
        papers.appendleft(current_paper)
        papers.append(first_paper)

    elif current_egg <= 0:
        papers.append(current_paper)
    elif current_egg + current_paper <= BOX_SIZE:
        boxes_count += 1

if boxes_count > 0:
    print(f"Great! You filled {boxes_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(egg) for egg in eggs])}")

if papers:
    print(f"Pieces of paper left: {', '.join([str(pe) for pe in papers])}")

