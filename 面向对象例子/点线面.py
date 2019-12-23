# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。

from math import sqrt

class Point(object):
    
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def moveToPoint(self, x, y):
        self._x = x
        self._y = y
    
    def moveBy(self, dx, dy):
        self._x += dx
        self._y += dy

    def distanceToPoint(self, other):
        dx = other._x - self._x
        dy = other._y - self._y
        return sqrt(dx ** 2 + dy ** 2)
    
    def __str__(self):
        return '(%s, %s)' %(str(self._x), str(self._y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.moveBy(-1, 2)
    print(p2)
    print(p1.distanceToPoint(p2))

if __name__ == '__main__':
    main()