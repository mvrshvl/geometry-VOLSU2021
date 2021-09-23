"""
Задание 3.
Пусть на плоскости задан многоугольник (необязательно выпуклый и необязательно ограниченный) и точка.
Найти расстояние от этой точки до многоугольника.
"""

import matplotlib.pyplot as plt
import random
import math

class Point:
    def __init__(self, x=None, y=None):
        self.x = random.randint(-15, 15) if not x else x
        self.y = random.randint(-15, 15) if not y else y

    def __str__(self):
        return f'({self.x},{self.y})'

    @classmethod
    def createPoint(cls):
        x = input("Enter x: ")
        y = input("Enter y: ")
        return cls(int(x), int(y))


class Line:
    def __init__(self, pointA=None, pointB=None):
        self.p1 = pointA if pointA else Point()
        self.p2 = pointB if pointB else Point()

    def __str__(self):
        return f'{self.p1} {self.p2}'


def distance(point, line):
    try:
        return abs(
            (line.p2.y - line.p1.y) * point.x - (line.p2.x - line.p1.x) *
            point.y + line.p2.x * line.p1.y - line.p2.y * line.p1.x) / math.sqrt((line.p2.y - line.p1.y) ** 2 + (line.p2.x - line.p1.x) ** 2)
    except ZeroDivisionError:
        return 0


def generatePoints():
    polygonPoints = []

    for _ in range(int(input('Enter count of random points: '))):
        polygonPoints.append(Point())

    return sorted(polygonPoints, key=lambda obj: math.atan2(obj.y, obj.x))


def calculate(point, polygonPoints):
    line = Line(polygonPoints[0], polygonPoints[1])
    d = distance(point, line)

    for i, point_fig in enumerate(polygonPoints[1:-1]):
        q_line = Line(point_fig, polygonPoints[i + 1])
        dq = distance(point, q_line)
        if dq < d and dq != 0:
            d = dq
            line = q_line

    q_line = Line(polygonPoints[0], polygonPoints[-1])
    dq = distance(point, q_line)

    if dq < d and dq != 0:
        d = dq
        line = q_line

    return line, d


def showPlot(point, polygonPoints, line):
    plt.scatter(point.x, point.y, color="red")

    for polygonPoint in polygonPoints:
        plt.scatter(polygonPoint.x, polygonPoint.y, color="green")

    plt.fill(
        [polygonPoint.x for polygonPoint in polygonPoints],
        [polygonPoint.y for polygonPoint in polygonPoints],
        fill=False
    )

    plt.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y])

    plt.show()


if __name__ == '__main__':
    polygonPoints = generatePoints()
    print([
        point.__str__() for point in polygonPoints
    ])

    point = Point.createPoint()

    line, dstnc = calculate(point, polygonPoints)

    print(f'Line {line.__str__()}\nDistance from point {point.__str__()} to polygon = {dstnc}')

    # install: sudo apt-get install python3-tk
    showPlot(point, polygonPoints, line)
