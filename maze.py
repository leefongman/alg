#!/usr/bin/env python3

import time
import os
#  移动方向列表
DIRECTION = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def getMap():
    #  迷宫创建
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
    """
    迷宫求解状态显示
    """
    #  将光标移动到第一行第一列
    print("\033[1;1H", end='', flush=True)
    #  状态显示过程
    for row in mazeMap:
        for ch in row:
            if ch == '@':
                #  红色高亮字符
                print("\033[31m" + ch + "\033[0m", end='', flush=True)
            else:
                print(ch, end='')
        print()


def getPos(mazeMap, ch):
    """
    返回特定字符所在的行列坐标
    """
    for row, rowCh in enumerate(mazeMap):
        for col, char in enumerate(rowCh):
            if char == ch:
                return [row, col]


def init(mazeMap, startCh, stopCh):
    """
    返回开始与结束字符的行列坐标
    """
    #  清屏
    print("\033[2J", end='', flush=True)

    return getPos(mazeMap, startCh), getPos(mazeMap, stopCh)


def maze(mazeMap, start, stop):
    """
    迷宫求解过程
    """
    showMap(mazeMap)
    time.sleep(0.1)

    for direct in DIRECTION:
        #  循环四个方向求解迷宫
        new = [start[0] + direct[0], start[1] + direct[1]]
        if mazeMap[new[0]][new[1]] == ' ':
            #  更新迷宫状态
            mazeMap[new[0]][new[1]] = '@'
            #  显示最新迷宫状态
            maze(mazeMap, new, stop)
        elif new == stop:
            #  迷宫成功求解,退出程序
            os._exit(0)

    mazeMap[start[0]][start[1]] = ' '
    showMap(mazeMap)
    time.sleep(0.1)


def main():
    """
    主程序
    """
    mazeMap = getMap()
    start, stop = init(mazeMap, 'S', 'E')
    maze(mazeMap, start, stop)


if __name__ == "__main__":
    main()
