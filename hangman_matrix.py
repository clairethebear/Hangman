"""Multi Dimensional List that will present the hangman graphic in the
terminal window
"""

def hangman_matrix(count, holder):

  # First beam
  if count == 1:
    for i in range(len(holder) - 1):
      holder[i][1] = 'x'
      holder[0][1] = ' '

  # Second Beam
  if count == 2:
    for x in range((len(holder) / 2) - 2):
      print x
      holder[1][x] = 'x'
      holder[1][0] = ' '

  # Rope
  if count == 3:
    for y in range((len(holder) /2) - 5):
      print y
      holder[y][6] = 'x'

  # Head
  if count == 4:
    holder[5][5] = 'x'
    holder[5][7] = 'x'
    holder[6][5] = 'x'
    holder[6][7] = 'x'
    holder[7][6] = 'x'

  # Body
  if count == 5:
    holder[8][6] = 'x'
    holder[9][6] = 'x'
    holder[10][6] = 'x'
    holder[11][6] = 'x'
    holder[12][6] = 'x'
    holder[13][6] = 'x'
    holder[14][6] = 'x'

  # Arms
  if count == 6:
    holder[10][7] = 'x'
    holder[10][8] = 'x'
    holder[10][5] = 'x'
    holder[10][4] = 'x'

  # Legs
  if count == 7:
    holder[14][7] = 'x'
    holder[14][5] = 'x'
    holder[15][5] = 'x'
    holder[16][5] = 'x'
    holder[17][5] = 'x'
    holder[15][5] = 'x'
    holder[15][7] = 'x'
    holder[16][7] = 'x'
    holder[17][7] = 'x'
    holder[15][7] = 'x'
    print "You loose Game Over!!"
  return holder

# holder = [[' ' for i in range(10)] for j in range(20)]
# count = 0
# while count < 7:
#
#   raw_input("test")
#   count += 1
#   holder = hangman_matrix(count, holder)
#   for i in holder:
#     print i
#   hangman_view = "".join(i)
#   print hangman_view

