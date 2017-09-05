#!/usr/bin/env python

def transverse(row, col):
    if col == 1:
        return "1×%d=%d\t" % (row, 1 * row)
    else:
        return transverse(row, col - 1) + "%d×%d=%d\t" % (col, row, col * row)

def vertical(row):
    if row == 1:
        return transverse(1, 1) + "\n"
    else:
        return vertical(row - 1) + transverse(row, row) + "\n"

if __name__ == "__main__":
    print(vertical(9))
