print("Print equilateral triangle pyramid using asterisk symbol")
size = int(input("Enter the number of rows: "))
m = (2 * size) - 2

for i in range(size):
    for j in range(m):
        print(" ",end=""),
    m =m - 1

    for j in range(i + 1):
        print("* ", end="")

    print("")