import math
import matplotlib.pyplot as mp
import numpy as n
from math import sqrt as s

class Octagon:
    def __init__(self,side):
        self.side = side
        self.corner = 135
        self.k = 1 + s(2)

    def RadiusAndAreaOfCircumscribedCircle(self):
        self.radius = self.side / (s(2- s(2)))
        self.square = math.pi * self.radius**2
        return self.radius, self.square

    def RadiusAndAreaOfAnInscribedCircle(self):
        self.radius = (self.side * self.k) / 2
        self.square = math.pi * self.radius**2
        return self.radius, self.square

    def PerimetrAndArea(self):
        self.perimetr = 8 * self.side
        self.area = 2 * self.side**2 * self.k
        return self.perimetr, self.area

    def draw(self):
        R, _ = self.RadiusAndAreaOfCircumscribedCircle()
        r, _ = self.RadiusAndAreaOfAnInscribedCircle()

        self.fig, ax = mp.subplots(figsize=(8, 8))
        self.circumCircle = mp.Circle((0, 0), R, fill=False, color='blue', linewidth=2.5)
        ax.add_patch(self.circumCircle)
        self.inscribedCircle = mp.Circle((0, 0), r, fill=False, color='green', linewidth=2.5)
        ax.add_patch(self.inscribedCircle)
        self.figure = n.linspace(0, 2 * n.pi, 8, endpoint=False) + n.pi / 8
        self.X = R * n.cos(self.figure)
        self.Y = R * n.sin(self.figure)
        self.XClosed = n.append(self.X, self.X[0])
        self.YClosed = n.append(self.Y, self.Y[0])
        ax.plot(self.XClosed, self.YClosed, color='red', linewidth=3)

        mp.title("Окружности и октагон") 
        mp.grid(True)
        mp.show()


