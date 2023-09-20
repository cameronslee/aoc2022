import math

X_HEAD = 0
Y_HEAD = 0
X_TAIL = 0
Y_TAIL = 0

with open('input.txt') as f:
  input = f.readlines()

locations = set()
for i in input:
  dir = i.split()[0]
  step = int(i.split()[1])
  print(dir, step)

  for j in range(step):
    # MOVE HEAD
    if dir == 'R':
      X_HEAD += 1 
    elif dir == 'L':
      X_HEAD -= 1 
    elif dir == 'U':
      Y_HEAD += 1 
    elif dir == 'D':
      Y_HEAD -= 1 

    # UPDATE TAIL
    DX = X_HEAD - X_TAIL
    DY = Y_HEAD - Y_TAIL

    if abs(DX) == 2 or abs(DX) + abs(DY) >= 3:
      X_TAIL += math.copysign(1,DX)
    if abs(DY) == 2 or abs(DX) + abs(DY) >= 3:
      Y_TAIL += math.copysign(1,DY)

    # RECORD LOCATION
    locations.add((X_TAIL, Y_TAIL))
  
print("LOCATIONS: ", len(locations))
