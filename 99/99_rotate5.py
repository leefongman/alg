for i in range(9, 0, -1):
    for j in range(1, i+1):
        print("%d×%d=%d" % (j, i, i*j),end="\t")
    print()
