from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4
    DASHES_COUNT = 11
    SYMBOL_FOR_LINE = '-'

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < self.MAX_PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1   # because we are starting from the 1st
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self):
        result = [
            self.DASHES_COUNT * self.SYMBOL_FOR_LINE
        ]

        for page in self.photos:
            result.append(('[] ' * len(page)).rstrip())
            result.append(self.DASHES_COUNT * self.SYMBOL_FOR_LINE)

        return '\n'.join(result)
