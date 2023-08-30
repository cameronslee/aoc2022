with open('input.txt') as f:
  lines = f.readlines()

x_plays= {'A': 1, 'B': 2, 'C': 3}
y_plays= {'X': 1, 'Y': 2, 'Z': 3}

# Part 1
total = 0

for l in lines:
  opp_play = l[0]
  your_play = l[2]
  
  shape_score = y_plays[your_play]

  outcome_score = 0

  if x_plays[opp_play] - y_plays[your_play] == 1 or x_plays[opp_play] - y_plays[your_play] == -2:
    outcome_score = 0 # loss
  elif x_plays[opp_play] == y_plays[your_play]:
    outcome_score = 3 # tie
  else:
    outcome_score = 6 # win

  total += (shape_score + outcome_score)

print("Part 1 Total Score: ", total)

# Part 2
total = 0
# Lose, Draw, Win
outcomes = {'X': 0, 'Y': 3, 'Z': 6}

for l in lines:
  opp_play = x_plays[l[0]]

  outcome_score = outcomes[l[2]]
  shape_score = 0

  # lose
  if outcome_score == 0:
    if opp_play == 1:
      shape_score = 3
    else:
      shape_score = opp_play - 1
  # draw
  elif outcome_score == 3:
    shape_score = opp_play 
  # win
  else:
    if opp_play == 3:
      shape_score = 1
    else:
      shape_score = opp_play + 1

  total += (shape_score + outcome_score)

print("Part 2 Total Score: ", total)
