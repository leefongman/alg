#!/usr/bin/env python3


"""
匹配用字典
"""
Dict = {")": "(", "]": "[", "}": "{", ">": "<"}


def preprocess(expression):
    if len(expression) == 0:
        return []

    p = preprocess(expression[:-1])

    if expression[-1] in Dict and p and Dict[expression[-1]] == p[-1]:
        p.pop()
    elif expression[-1] in Dict.values():
        p.append(expression[-1])

    return p


def metch(expression):
    return not preprocess(expression)


if __name__ == "__main__":
    expression = ")("
   print(metch(expression))
