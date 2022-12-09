M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
elem = 1
a = None
class stack:
    def __init__(self, M):
        self.M = M
        self.last = len(M) - 1

    def push(self, elem):
        self.M.append(elem)
    def peek(self, a):
        a = self.M[-1]
        return a
    def pop(self, a):
        a = self.M[-1]
        self.M.pop(-1)
        return a
class queue:
    def __init__(self, M):
        self.last = len(M) - 1
        pass

    def peek(self):
        return M[0]

    def enqueue(self):
        return M.append(obj)

    def dequeue(self):
        M.pop(M[0])
        M.append(M[0])


queue = queue(M)
queue.peek()
# obj = queue.peek()
print(queue.peek())
