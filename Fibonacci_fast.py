class Solution:
    
    def fib(self, N: 'int') -> 'int':
        if N is 0:
            return 0
        elif N is 1:
            return 1
        elif N > 1:
            val = [1, 0]
            i = 0
            while i < (N-1):
                val.insert(0, sum(val))
                val.pop()
                i += 1
            return val[0]
        
