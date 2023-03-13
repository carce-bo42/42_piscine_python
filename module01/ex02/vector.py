from typing import List, Tuple
from copy import deepcopy

# UNDERSTANDING ZERRO ARRAY INITIALIZATION
# rows, cols = 3,6
# my_matrix = [([0]*cols) for i in range(rows)]
# This [0]*cols) produces a one-dimensional list of zeros.
# The for loop creates as many elements as rows there are.

class Vector:
    
    """
    An all purpose vector class.

    shape notation : (column, rows)

    column vector: [[1.], [2.], [3.]] ==> (3, 1)
    row vector:      [[1., 2., 3.]]   ==> (1, 3)

    self.shape[0] : columns
    self.shape[1] : rows

    """

    def __init__(self) -> None:
        pass

    def __init__(self, values):
        self.shape = (len(values), len(values[0]))
        self.values = values
    
    def __add__(self, o):

        if self.shape == o.shape:
            result = [([0.] * self.shape[1]) for i in range(self.shape[0])]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = self.values[i][j] + o.values[i][j]
            return Vector(result)
        else:
            raise ValueError("Vector.__add__: Different shape")

    def __sub__(self, o):

        if self.shape == o.shape:
            result = [([0.] * self.shape[1]) for i in range(self.shape[0])]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = self.values[i][j] - o.values[i][j]
            
            return Vector(result)
        else:
            raise ValueError("Vector.__sub__: Different shape")
    
    def __mul__(self, scalar):
        
        result = [([0.] * self.shape[1]) for i in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self.values[i][j] * scalar
        
        return Vector(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        
        if scalar == 0:
            raise ZeroDivisionError("Vector.__truediv__")
        
        if (self.shape[0] > 1):
            result = [([0.] * self.shape[1]) for i in range(self.shape[0])]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = self.values[i][j] / scalar
        return Vector(result)

    def __rtruediv__(self, scalar):
        raise NotImplementedError("Vector.__rtruediv__")

    def dot(self, o) -> int:

        if self.shape == o.shape:
            ret = 0
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    ret += self.values[i][j] * o.values[i][j]
            return ret
        else:
            raise ValueError("Vector.dot different shape")

    def T(self):

        transposed = [([0.] * self.shape[0]) for i in range(self.shape[1])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                transposed[j][i] += self.values[i][j]
        return Vector(transposed)

    def __str__(self):
        return f'Vector({str(self.values)})'
