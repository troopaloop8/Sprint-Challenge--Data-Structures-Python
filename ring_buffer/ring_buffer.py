class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data = self.data + [item]
            self.counter += 1
        else:
            if self.counter == 5:
                self.counter = 0
            i = (self.counter - self.capacity)
            self.counter += 1

            self.data[i] = item

    def get(self):
        return self.data

michael_buffer = RingBuffer(5)

michael_buffer.append(25)
michael_buffer.append(54)
michael_buffer.append(34)
michael_buffer.append(14)
michael_buffer.append(6)



print(michael_buffer.get())
michael_buffer.append(64)
print(michael_buffer.get())
michael_buffer.append(67)
print(michael_buffer.get())
michael_buffer.append(1)
print(michael_buffer.get())
michael_buffer.append(42)
print(michael_buffer.get())
michael_buffer.append(99)
print(michael_buffer.get())
michael_buffer.append(6745763)
print(michael_buffer.get())
michael_buffer.append(2356324)
print(michael_buffer.get())
michael_buffer.append(9876534321)
print(michael_buffer.get())