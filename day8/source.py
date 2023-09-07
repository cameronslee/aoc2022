with open('input.txt') as f:
  input = f.readlines()

map = []
for l in input:
  temp = []
  for c in l[:-1]:
    temp.append(c)
  map.append(temp)

m = len(map)
n = len(map[0])

# Part 1
def left(map,root,i,j):
  for a in range(j-1,-1,-1):
    if map[i][a] >= root:
      return False
  return True

def right(map,root,i,j):
  for a in range(j+1,n,1):
    if map[i][a] >= root:
      return False
  return True

def up(map,root,i,j):
  for a in range(i-1,-1,-1):
    if map[a][j] >= root:
      return False
  return True

def down(map,root,i,j):
  for a in range(i+1,n,1):
    if map[a][j] >= root:
      return False
  return True

def visible(map,root,i,j):
  if left(map,root,i,j) or right(map,root,i,j) or up(map,root,i,j) or down(map,root,i,j):
    return True
  return False

count = 0
for i in range(1,m-1):
  for j in range(1,n-1):
    root = map[i][j]
    if visible(map,root,i,j):
      count += 1

exterior_count = (m*2 + n*2) - 4
print("Count: ", count + exterior_count)

# Part 2
def left(map,root,i,j):
  score = 0
  for a in range(j-1,-1,-1):
    score += 1
    if map[i][a] >= root:
      break
  return score

def right(map,root,i,j):
  score = 0
  for a in range(j+1,n,1):
    score += 1
    if map[i][a] >= root:
      break
  return score

def up(map,root,i,j):
  score = 0
  for a in range(i-1,-1,-1):
    score += 1
    if map[a][j] >= root:
      break
  return score

def down(map,root,i,j):
  score = 0
  for a in range(i+1,n,1):
    score += 1
    if map[a][j] >= root:
      break
  return score

def score(map,root,i,j):
  return left(map,root,i,j) * right(map,root,i,j) * up(map,root,i,j) * down(map,root,i,j)

max_score = 0
for i in range(1,m-1):
  for j in range(1,n-1):
    root = map[i][j]
    print(score(map,root,i,j))
    max_score = max(max_score, score(map,root,i,j))
    print(max_score)

print("Max Scenic Score: ", max_score)
