#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    """
    算术运算符:
        +   add
        -   sub
        *   mul
        /   truediv
        //  floordiv
        %   mod
        **  pow
        >>  rshift
        <<  lshift
        &   and
        |   or
        ^   xor
    """
    #  重载对象为运算符左值
    def __add__(self, obj):
        if isinstance(obj, Point):
            return Point(self.x + obj.x, self.y + obj.y)
        elif type(obj) == int:
            return Point(self.x + obj, self.y + obj)

    #  重载对象为运算符右值
    def __radd__(self, obj):
        if isinstance(obj, Point):
            return Point(self.x + obj.x, self.y + obj.y)
        elif type(obj) == int:
            return Point(self.x + obj, self.y + obj)

    #  增量赋值运算符(eg: +=)
    def __iadd__(self, obj):
        if isinstance(obj, Point):
            self.x += obj.x
            self.y += obj.y
        elif type(obj) == int:
            self.x += obj
            self.y += obj

        return self

    """
    比较运算符
    <   lt  (less than)
    <=  le  (less than or equal to)
    >   gt  (greater than)
    >=  ge  (greater than or equal to)
    ==  eq  (equal to)
    !=  ne  (not equal to)
    """
    def __eq__(self, obj):
        return isinstance(obj, Point) and self.x == obj.x and self.y == obj.y

    """
    单目运算符
    +                               pos         (positive)
    -                               neg         (negative)
    ~                               invert
    obj[attr_name]                  getitem
    obj[attr_name] = attr_value     setitem
    del obj[attr_name]              delitem
    ()                              call
    """
    def __neg__(self):
        self.x = -self.x
        self.y = -self.y

    def __getitem__(self, idx):
        return getattr(self, idx)

    def __setitem__(self, idx, val):
        setattr(self, idx, val)

    def __delitem__(self, idx):
        delattr(self, idx)

    def __call__(self, idx):
        return getattr(self, idx)


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(2, 3)
    print(p1.get(), "+", p2.get(), "=", (p1 + p2).get())
    print(p1.get(), "+ 1 =", (p1 + 1).get())
    print("p1 =", p1.get())
    p1 += p2
    print("p1 =", p1.get(), "[" + str(p1.get()), "+=", str(p2.get()) + "]")
    print(p2.get(), "==", p3.get(), "?", p2 == p3)
    print(str(p1.get()) + "[x] =", p1["x"])
    print(str(p1.get()) + "(x) =", p1("x"))
    print("p1 =", p1.get())
    p1["x"] = 10
    #  del p1["x"]
    print("p1 =", p1.get())

