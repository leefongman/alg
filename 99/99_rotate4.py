for i in range(1, 10):
    for j in range(9, i-1, -1):
        print(("%d×%d=%d" % (i, j, i*j)).ljust(8),end="")
    print()
