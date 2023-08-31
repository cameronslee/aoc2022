import numpy as np
with open('input.txt') as f:
  lines = f.readlines()

# Part 1
uppers = list(map(chr, range(65, 90+1)))
lowers = list(map(chr, range(97, 122+1)))

priorities = {x: ord(x)-96 for x in lowers} | {x: ord(x)-38 for x in uppers}

sum = 0

for l in lines:
  length = len(l)-1 #exclude newline char
  mid = int(length/2)
  c1 = l[:mid]
  c2 = l[mid:length]

  d1 = set()
  d2 = set()
  for i,j in zip(c1,c2):
    d1.add(i)
    d2.add(j)

  for i in d1:
    if i in d2:
      sum += priorities[i]

print("Part 1 Sum of priorities: ", sum)

# Part 2
e1, e2, e3 = "", "", ""
index = 0
sum = 0

for l in lines:
  index += 1
  if index == 1:
    e1 = l[:-1]
  elif index == 2:
    e2 = l[:-1]
  elif index == 3:
    e3 = l[:-1]

    d1 = set()
    d2 = set()
    d3 = set()

    for i in e1:
      d1.add(i)
    for i in e2:
      d2.add(i)
    for i in e3:
      d3.add(i)

    for i in d1:
      if i in d2 and i in d3:
        sum += priorities[i]

    # reset for new group
    e1, e2, e3 = "", "", ""
    index = 0

print("Part 2 Sum of priorities: ", sum)
