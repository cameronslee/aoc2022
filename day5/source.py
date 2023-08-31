with open('input.txt') as f:
  lines = f.readlines()

# Part 1
stacks = [[] for i in range(9)]

read_drawing = True
read_ins = False

for l in lines:
  # Set up stacks
  if read_drawing:
    if len(l) > 2 and l[1] == '1':
      for s in stacks:
        s.reverse()
      read_drawing = False
      read_ins = True
      print(stacks)
      continue

    foo = []
    for i in range(0,36, 4):
      foo.append(l[i:i+4])
    
    for i in range(len(foo)):
      if foo[i][1] != ' ':
        stacks[i].append(foo[i][1])
  
  if read_ins and l[0] == 'm':
    l = l[:-1]
    ins = l.split(' ')

    num_op = int(ins[1])
    src = int(ins[3]) - 1
    dst = int(ins[5]) - 1

    for i in range(0,num_op):
      temp = stacks[src].pop()
      stacks[dst].append(temp)

ans = ""
for s in stacks:
  tmp = s.pop()
  ans += tmp

print("Part 1 ans: ", ans)

# Part 2
stacks = [[] for i in range(9)]
read_drawing = True
read_ins = False

for l in lines:
  # Set up stacks
  if read_drawing:
    if len(l) > 2 and l[1] == '1':
      for s in stacks:
        s.reverse()
      read_drawing = False
      read_ins = True
      print(stacks)
      continue

    foo = []
    for i in range(0,36, 4):
      foo.append(l[i:i+4])
    
    for i in range(len(foo)):
      if foo[i][1] != ' ':
        stacks[i].append(foo[i][1])
  
  if read_ins and l[0] == 'm':
    l = l[:-1]
    ins = l.split(' ')

    num_op = int(ins[1])
    src = int(ins[3]) - 1
    dst = int(ins[5]) - 1
    
    temp = []
    for i in range(0,num_op):
      t = stacks[src].pop()
      temp.append(t)
    
    temp.reverse()
    for i in temp:
      stacks[dst].append(i)

ans = ""
for s in stacks:
  tmp = s.pop()
  ans += tmp

print("Part 2 ans: ", ans)
