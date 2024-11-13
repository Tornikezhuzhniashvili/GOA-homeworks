# დავალება 4 : 
# შექმნით რომბი
#   *
#  ***
# *****
#  ***
#   *

rows = [1, 3, 5, 3, 1]
spaces = [3, 2, 1, 2, 3] 

for i in range(len(rows)):
    print(" " * spaces[i] + "*" * rows[i])