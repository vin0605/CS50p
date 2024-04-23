class Jar:
    def __init__(self, capacity=12):
        #default capacity is 12, but it could be overridden
        # cookie = Jar(10)
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError ('Invalid number')
        
        self._capacity = capacity
        self.number = 0

    def __str__(self):
        return '🍪' * self.number

    def deposit(self, n):
        if isinstance(n, int) and n > 0 and self.number + n <= self._capacity:
            self.number += n
        else:
            raise ValueError ('Invalid number')

    def withdraw(self, n):
        if isinstance(n, int) and n > 0 and self.number - n >= 0:
            self.number -= n
        else:
            raise ValueError ('Invalid number')

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.number