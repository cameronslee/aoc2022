from collections import defaultdict

with open('input.txt') as f:
  lines = f.readlines()

data = defaultdict(int)
stack = []

for line in lines:
  if line.startswith('$ ls') or line.startswith('dir'):
    continue
  if line.startswith('$ cd'):
    d = line.split()[2]
    if d == '..':
      stack.pop()
    else:
      path = f'{stack[-1]}_{d}' if stack else d
      stack.append(path)
  else:
    size, file = line.split()
    for path in stack:
      data[path] += int(size)

total = 0
for key in data:
  if data[key] <= 100000:
    print(key, data[key])
    total += data[key]

needed_space = 30000000 - (70000000 - data['/'])
for s in sorted(data.values()):
  if s > needed_space:
    print("Part 2 size: ", s)
    break

print("Part 1 total: ", total)


    
    

