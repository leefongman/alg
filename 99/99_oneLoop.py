i = 1
j = 1
while j <= 9:
	print("%d*%d=%d" % (i, j, i*j), end="\t")
	if i == j:
		i = 0
		j += 1
		print()
	i += 1
