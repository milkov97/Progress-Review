# What will be the output of the following code? Why?
class Counter:
    def __init__(self):
        self._updates = 0
        self._count = 0
    
    @property
    def updates(self):
        return self._updates

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.increment()
        self._count = value

    def increment(self):
        self._updates += 1

c = Counter()
c.count = 1
c.count = 10
print(c.count)
print(c.updates)
