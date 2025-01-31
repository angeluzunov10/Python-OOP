class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_index = 0
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= self.start_index:
            return self.iterable[self.index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)