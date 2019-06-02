class Heap:

    def __init__(self):
        self.size = 0
        self.result = []

    def siftDown(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.size and self.result[right] > self.result[left]:
                j = right
            if self.result[i] >= self.result[j]:
                break
            self.result[i], self.result[j] = self.result[j], self.result[i]
            i = j

    def siftUp(self, i):
        while i > 0 and self.result[i] > self.result[(i - 1) // 2]:
            self.result[i], self.result[(i - 1) // 2] = self.result[(i - 1) // 2], self.result[i]
            i = (i - 1) // 2

    def insert(self, n):
        self.size += 1
        self.result.append(n)
        self.siftUp(self.size - 1)

    def extract_max(self):
        if not self.result:
            return
        last = self.result[0]
        self.result[0] = self.result.pop(self.size - 1)
        self.size -= 1
        self.siftDown(0)
        return last


if __name__ == '__main__':
    with open('example_heap.txt') as f:
        n = int(f.readline().strip())
        commands = [f.readline().strip() for _ in range(n)]

    heap = Heap()
    for command in commands:
        if command.startswith("Insert"):
            command = command.split()
            heap.insert(int(command[1]))
        else:
            result = heap.extract_max()
            if result:
                print(result)
