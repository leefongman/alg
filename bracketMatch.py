#!/usr/bin/env python3


"""
括号匹配,判断表达式中括号是否一一匹配,包含小括号/中括号/花括号/尖括号
"""
Dict = {")": "(", "]": "[", "}": "{", ">": "<"}


def preprocess(expression):
    """
    左括号进栈,遇到与最新进栈的右括号时出栈,返回最终列表
    """
    if len(expression) == 0:
        return []
    #  去除最后一个字符,用于递归
    p = preprocess(expression[:-1])
    #  出栈处理
    if expression[-1] in Dict and p and Dict[expression[-1]] == p[-1]:
        p.pop()
    #  进栈处理
    elif expression[-1] in Dict.values():
        p.append(expression[-1])

    return p


def metch(expression):
    """
    判断预处理后的列表是否为空列表,是则表示所有括号都一一匹配
    """
    return not preprocess(expression)


if __name__ == "__main__":
    expression = ")("
    print(metch(expression))
