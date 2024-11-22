class Fibonacci:
    def __init__(self, len=0):
        self.len = len
        self.__fibs = [0 for _ in range(len)]
        self.__fibs[1] = 1
        self.init_sequence_fibonacci()
        self.__index = 0

    def init_sequence_fibonacci(self) -> None:
        for i in range(2, self.len):
            self.__fibs[i] = self.__fibs[i-2] + self.__fibs[i-1]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> int:
        if self.__index < self.len:
            result = self.__fibs[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration

    @property
    def fibs(self):
        return self.__fibs

    def __str__(self):
        return f"{self.__fibs}"

c = Fibonacci(10)

for i in c:
    print(i)