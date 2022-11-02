class Deque:
    def __init__(self):
        MX = 1000005  # In Coding Test -> 배열을 충분히 크게 잡으면 된다.
        self.dat = [0] * (2 * MX + 1)
        self.head, self.tail = MX, MX

    def push_front(self, x):
        self.head -= 1
        self.dat[self.head] = x

    def push_back(self, x):
        self.dat[self.tail] = x
        self.tail += 1

    def pop_front(self):
        self.head += 1

    def pop_back(self):
        self.tail -= 1

    def front(self):
        return self.dat[self.head]

    def back(self):
        return self.dat[self.tail - 1]

    def size(self):
        return self.tail - self.head

    def test(self):
        self.push_back(1)
        self.push_back(2)
        self.push_back(3)
        self.push_front(4)
        self.push_front(5)
        print(self.front())
        print(self.back())
        print(self.size())


deque = Deque()
deque.test()
print(deque.dat[1000001:1000010])
