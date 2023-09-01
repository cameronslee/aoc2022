with open('input.txt') as f:
  input = f.read()

# Part 1
index = 0
for c in range(0,len(input)):
  unique_count = 0
  unique = list()
  print(c)
  for i in range(c, c+4):
    if input[i] not in unique:
      unique.append(input[i])
      print(unique)
      unique_count += 1
    else:
      break

  if unique_count == 4:
    print(c+4)
    break

# Part 2
for c in range(0,len(input)):
  unique_count = 0
  unique = list()
  print(c)
  for i in range(c, c+14):
    if input[i] not in unique:
      unique.append(input[i])
      print(unique)
      unique_count += 1
    else:
      break

  if unique_count == 14:
    print(c+14)
    break
