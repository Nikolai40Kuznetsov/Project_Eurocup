from shuffle import champions_qual
from games import group_shuffle
import random as ran
a = champions_qual()
b = group_shuffle(a)
c = 0
d = 0
matrix = []
for i in range(32):
   row = [b[c][d][0]] + [0] * 32
   matrix.append(row)
   if d == 3:
      d = -1
      c += 1
   d += 1
for i in range(32):
   for j in range(4):
      x = ran.randint(0, 7)
      place = 1 + 8 * j + x
      while i == 1 + 8 * j + x:
         x = ran.randint(0, 7)
         place = 1 + 8 * j + x
      matrix[i][place] += 1
print(matrix)