from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            album_instance = next(filter(lambda a: a.name == album_name, self.albums))

        except StopIteration:
            return f"Album {album_name} is not found."

        if album_instance.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(album_instance)

        return f"Album {album_name} has been removed."

    def details(self) -> str:
        info = [f"Band {self.name}"]
        info.extend([album.details() for album in self.albums])

        return '\n'.join(info)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
