#!/usr/bin/python3

class CountedIterator:

    def __init__(self, iterable):
        self.count = 0
        self.it = iter(iterable)
    
    def __next__(self):
        self.count += 1
        return next(self.it)
    
    def __iter__(self):
        return self
    
    def get_count(self):
        return self.count
    