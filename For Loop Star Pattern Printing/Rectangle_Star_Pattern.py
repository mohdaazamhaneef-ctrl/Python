# Program 2: Print a 4 x 6 rectangle star pattern

row = 4
column = 6

for i in range(1, row + 1):
    for j in range(1, column + 1):
        print("*", end=" ")
    print()
