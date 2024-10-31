class vowels:
    def __init__(self, _string):
        self._string = _string
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.index = -1
        self.vowels_in_string = [v for v in self._string if v.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_in_string):
            return self.vowels_in_string[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)