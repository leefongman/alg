for i in range(9, 0, -1):
    for a in range(9-i):
        print("".ljust(8),end="")
    for j in range(i, 0, -1):
        print(("%d×%d=%d" % (j, i, i*j)).ljust(8),end="")
    print()
