with open('input.txt') as f:
  lines = f.readlines() 

total = 0
# Part 1
for l in lines:
  l = l[:-1]
  assignments = l.split(',')
  print(assignments)

  r1 = assignments[0].split('-')
  r2 = assignments[1].split('-')
  
  lo1 = int(r1[0])
  lo2 = int(r2[0])

  hi1 = int(r1[1])
  hi2 = int(r2[1])

  if (lo1 >= lo2 and hi1 <= hi2) or (lo2 >= lo1 and hi2 <= hi1):
    total += 1

print("Part 1 Total: ", total)

# Part 2
total = 0
for l in lines:
  l = l[:-1]
  assignments = l.split(',')
  print(assignments)

  r1 = assignments[0].split('-')
  r2 = assignments[1].split('-')
  
  lo1 = int(r1[0])
  lo2 = int(r2[0])

  hi1 = int(r1[1])
  hi2 = int(r2[1])

  if (lo1 >= lo2 and lo1 <= hi2) or (lo2 >= lo1 and lo2 <= hi1):
    total += 1

print("Part 2 Total: ", total)
