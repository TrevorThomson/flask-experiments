
'''
class Fibonacci
Usage:
    fibo = Fibonacci()
    sum = fibo.sum(f)
    series = fibo.series(f)
'''

class Fibonacci:
    def __init__(self) -> None:
        pass

    def series(self, f):
        '''
        Build and return the Fibonacci series to f
        '''
        if f < 0:
            raise ValueError('Input must be >= 0')
        
        n_elems = f + 1

        output = []
        a = 0
        b = 1
        for i in range(n_elems):
            if i == 0:
                output.append(a)
            if i == 1:
                output.append(b)
            if i > 1:
                c = a + b
                output.append(c)
                a = b
                b = c

        return output

    def sum(self, f):
        '''
        Compute the sum of the Fibonacci series to f
        '''
        return sum(self.series(f))
    