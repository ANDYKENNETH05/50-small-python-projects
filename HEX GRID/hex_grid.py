"""Hex Grid, by Al Sweigart al@inventwithpython.com
Displays a simple tessellation of a hexagon grid.
"""

X_REPEAT = 10
Y_REPEAT = 10

for y in range(Y_REPEAT):
    for x in range (X_REPEAT):
        print(r'/ \_' , end='')
    print()

    for x in range (X_REPEAT):
        print(r'\_/ ', end='')
    print()