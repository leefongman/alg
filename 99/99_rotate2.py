for i in range(1, 10):
    for a in range(1, 10-i):
        print("".ljust(8),end="")
    for j in range(i, 0, -1):
        print(("%d×%d=%d" % (j, i, j*i)).ljust(8),end="")
    print()
