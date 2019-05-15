from typing import List
from utils import Vector

#DEPRECATED! Use numpy!!
#3x3 ROW MAJOR matrix
class Matrix:

    #vectors represent columns
    vectors = [] # type: List[Vector]

    #may need a way to construct from Vectors but idk
    def __init__(self, m00 = 0, m01 = 0, m02 = 0,
            m10 = 0, m11 = 0, m12 = 0,
            m20 = 0, m21 = 0, m22 = 0):
        #this may need some checking for row vs column major. stuff confuses me
        self.vectors.append(Vector(m00, m10, m20))
        self.vectors.append(Vector(m01, m11, m21))
        self.vectors.append(Vector(m02, m12, m22))

    # returns a COLUMN
    def __getitem__(self, item):
        return self.vectors[item]

    def __setitem__(self, key, value):
        self.vectors[key] = value

    def set_all_to_num(self, val = 0):
        self[0] = self[1] = self[2] = Vector(val, val, val)

    #I don't think we need this so I'm not gonna bother
    def det(self):
        # return -A(0,2)*A(1,1)*A(2,0) + A(0,1)*A(1,2)*A(2,0) +
        #     A(0,2)*A(1,0)*A(2,1) - A(0,0)*A(1,2)*A(2,1) -
        #     A(0,1)*A(1,0)*A(2,2) + A(0,0)*A(1,1)*A(2,2) ;
        raise NotImplementedError()

    def norm(self) -> float:
        return sqrt(self[0].normSquared() +
                    self[1].normSquared() +
                    self[2].normSquared())

    # may need some checking
    def __neg__(self):
        return Matrix(-self[0][0], -self[1][0], -self[2][0],
                      -self[0][1], -self[1][1], -self[2][1],
                      -self[0][2], -self[1][2], -self[2][2])

    def __sub__(self, other):
        newMatrix = Matrix()
        for i in range(3):
            for j in range(3):
                newMatrix[j][i] = self[j][i] - other[j][i]
        return newMatrix

    def __add__(self, other):
        newMatrix = Matrix()
        for i in range(3):
            for j in range(3):
                newMatrix[j][i] = self[j][i] + other[j][i]
        return newMatrix

    def __radd__(self, other):
        return self.__add__(other)

    #might need some double checking
    def __mul__(self, other):
        if isinstance(other, float):
            newMatrix = Matrix()
            for i in range(3):
                for j in range(3):
                    newMatrix[j][i] = self[j][i] * other
            return newMatrix
        elif isinstance(other, Matrix):
            newMatrix = Matrix()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        newMatrix[j][i] += self[k][i] * other[j][k]
            return newMatrix
        elif isinstance(other, Vector):
            return other[0]*self[0] + other[1]*self[1] + other[2]*self[2]

    def T(self):
        newMatrix = Matrix()
        for i in range(3):
            for j in range(3):
                newMatrix[j][i] = self[i][j]
        return newMatrix

    #uhhh, let's just say we don't need an inverse.
    def inv(self):
        # B(0, 0) = -A(1, 2) * A(2, 1) + A(1, 1) * A(2, 2);
        # B(0, 1) = A(0, 2) * A(2, 1) - A(0, 1) * A(2, 2);
        # B(0, 2) = -A(0, 2) * A(1, 1) + A(0, 1) * A(1, 2);
        # B(1, 0) = A(1, 2) * A(2, 0) - A(1, 0) * A(2, 2);
        # B(1, 1) = -A(0, 2) * A(2, 0) + A(0, 0) * A(2, 2);
        # B(1, 2) = A(0, 2) * A(1, 0) - A(0, 0) * A(1, 2);
        # B(2, 0) = -A(1, 1) * A(2, 0) + A(1, 0) * A(2, 1);
        # B(2, 1) = A(0, 1) * A(2, 0) - A(0, 0) * A(2, 1);
        # B(2, 2) = -A(0, 1) * A(1, 0) + A(0, 0) * A(1, 1);
        #
        # B /= det();
        #
        # return B;
        raise NotImplementedError()

    @classmethod
    def identity(cls):
        return Matrix(1, 0, 0,
                      0, 1, 0,
                      0, 0, 1)

    #not sure if needed
    def crossProduct(self):
        # u is a vector
        # B(0, 0) = 0.;
        # B(0, 1) = -u.z;
        # B(0, 2) = u.y;
        # B(1, 0) = u.z;
        # B(1, 1) = 0.;
        # B(1, 2) = -u.x;
        # B(2, 0) = -u.y;
        # B(2, 1) = u.x;
        # B(2, 2) = 0.;
        #
        # return B;
        raise NotImplementedError()

    @classmethod
    # the original method uses some weird pointer arithmetic, idk how it translates exactly but w/e.
    # As a result, it may produce what is actually the transpose of the outer mult of two vectors
    def outer(cls, u: Vector, v: Vector):
        return Matrix(u.x * v.x, u.y*v.x, u.z*v.x,
                      u.x * v.y, u.y*v.y, u.z*v.y,
                      u.x * v.z, u.y*v.z, u.z*v.z)



