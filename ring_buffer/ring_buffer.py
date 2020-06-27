class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.ring = []

    def append(self, item):
        if self.counter < self.capacity:
            self.ring.append(item)
        else:
            self.ring[self.counter % (self.capacity)] = item
        self.counter += 1

    def get(self):
        return self.ring
