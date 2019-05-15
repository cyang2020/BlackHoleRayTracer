from dataclasses import dataclass
from math import sqrt

#DEPRECATED! Use Numpy!!
@dataclass
class Vector:
    x: float = 0
    y: float = 0
    z: float = 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rsub__(self, other):
        raise RuntimeError("wut")

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other: float):
        return self.__mul__(1.0/other)

    def norm(self) -> object:
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normSquared(self) -> float:
        return self.x*self.x + self.y*self.y + self.z*self.z

    def normalize(self):
        norm = self.norm()
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def unit(self):
        return self / self.norm()

    def __getitem__(self, item):
        switch = {0 : self.x, 1: self.y, 2: self.z}
        return switch[item]

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise RuntimeError("Not a valid index")


