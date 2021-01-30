class Vector:
    """ Represent a vector in a multidimensional space"""

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        """ Return the dimension of the vector """
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of the vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        """ Return sum of two vectors"""
        if len(self) != len(other):  # relies on the __len__ method already implemented
            raise ValueError('Dimensions must be equivalent')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """ Return True if vectors has the same coordinates as other"""
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other  # rely on __eq__ method
        
    def __str__(self):
        """ Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'


print([0]*10)