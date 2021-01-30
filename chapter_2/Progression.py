class Progression:
    """ Iterator producing a generic progression """
    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        """ Update self._current to a new value

        This should be overridden by a sublcass to customize progression.

        By convention if current is et to None this designates the end of a finite progression.
        """
        self._current += 1
    
    def __next__(self):
        """ Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self

    def print_progression(self, n):
        """ Print next n values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))
        

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):

    def __init__(self, base,start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *=  self._base
        

class FibonacciProgression(Progression):

    def __init__(self, prev1=0, prev2=1):
        super().__init__()
        self._prev1 = prev1
        self._prev2 = prev2

    def _advance(self):
        self._prev1 = self._prev2
        self._prev2 = self._current
        self._current = self._prev1 + self._prev2
       
        
        


volume = FibonacciProgression()

volume.print_progression(9)
