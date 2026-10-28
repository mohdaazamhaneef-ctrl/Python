# Program 10: Diamond star pattern

n = 5

for i in range(1, 2 * n):
    if i <= n:
        star = i
    else:
        star = 2 * n - i

    space = n - star

    for j in range(space):
        print(" ", end=" ")

    for k in range(2 * star - 1):
        print("*", end=" ")

    print()
