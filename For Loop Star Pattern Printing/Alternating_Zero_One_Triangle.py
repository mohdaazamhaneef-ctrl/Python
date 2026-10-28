# Program 8: Alternating 0 and 1 triangle

n = 5

for i in range(1, n + 1):
    for j in range(0, i):
        print((i + j) % 2, end=" ")
    print()
