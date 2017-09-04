for i in range(9, 0, -1):
    for a in range(1, i):
        print("".ljust(8),end="")
    for j in range(i, 10):
        print(("%d×%d=%d" % (i, j, i*j)).ljust(8),end="")
    print()
