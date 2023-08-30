with open('input.txt') as f:
  lines = f.readlines()

data = list()
cur = 0

for l in lines:
  if l == '\n':
    data.append(cur)
    cur = 0
  else:
    cur += int(l)

data.sort(reverse=True)

print("Top Elf: ", data[0])
print("Top Three Total: ", (data[0]+data[1]+data[2]))
