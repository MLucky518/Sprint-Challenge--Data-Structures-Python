class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.oldest] = item
        self.oldest = (self.oldest + 1) % self.capacity

    def get(self):
        return self.data
