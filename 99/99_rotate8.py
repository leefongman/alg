for i in range(9, 0, -1):
    for j in range(9, i-1, -1):
        print("%d×%d=%d" % (i, j, i*j),end="\t")
    print()
