import math


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)] # Matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for i in range(len(self.photos)):
            if len(self.photos[i]) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                self.photos[i].append(label)

                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        else:
            return "No more free slots"

    def display(self) -> str:
        result = "-" * 11 + "\n"

        for page_index in range(len(self.photos)):
            result += (' '.join(["[]" for _ in range(len(self.photos[page_index]))])) + "\n"
            result += "-" * 11 + "\n"

        return result

