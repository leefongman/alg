#!/usr/bin/env python3

def createPickList(s):
    Dict = {")": "(", "]": "[", "}": "{", ">": "<"}
    if len(s) == 0:
        return []

    p = createPickList(s[:-1])

    if s[-1] in Dict:
        if Dict[s[-1]] == p[-1]:
            p.pop()
    elif s[-1] in Dict.values():
        p.append(s[-1])

    return p


def pick(s):
    return False if createPickList(s) else True


if __name__ == "__main__":
    pass
