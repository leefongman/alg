#!/usr/bin/env python3

import time
import os

DIRECTION = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def getMap():
    m = [
        "#####################",
        "#     ##          #S#",
        "# ###  # ######## # #",
        "# #  # # ##    ## # #",
        "# ## # # ## ## ## # #",
        "# #  # # ##  # ## # #",
        "#   ## # ## ##    # #",
        "### ## # ########## #",
        "#E  ##              #",
        "#####################"
        ]

    return [list(s) for s in m]


def showMap(mazeMap):
    print("\033[1;1H", end='', flush=True)
    for row in mazeMap:
        for ch in row:
            if ch == '@':
                print("\033[31m" + ch + "\033[0m", end='', flush=True)
            else:
                print(ch, end='')
        print()


def getPos(mazeMap, ch):
    for row, rowCh in enumerate(mazeMap):
        for col, char in enumerate(rowCh):
            if char == ch:
                return [row, col]


def init(mazeMap, startCh, stopCh):
    print("\033[2J", end='', flush=True)
    return getPos(mazeMap, startCh), getPos(mazeMap, stopCh)


def maze(mazeMap, start, stop):
    showMap(mazeMap)
    time.sleep(0.1)

    for direct in DIRECTION:
        new = [start[0] + direct[0], start[1] + direct[1]]
        if mazeMap[new[0]][new[1]] == ' ':
            mazeMap[new[0]][new[1]] = '@'
            maze(mazeMap, new, stop)
        elif new == stop:
            os._exit(0)

    mazeMap[start[0]][start[1]] = ' '
    showMap(mazeMap)
    time.sleep(0.1)


def main():
    mazeMap = getMap()
    start, stop = init(mazeMap, 'S', 'E')
    maze(mazeMap, start, stop)


if __name__ == "__main__":
    main()
