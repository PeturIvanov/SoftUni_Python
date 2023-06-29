from spoopify.song import Song

class Album:
    def __init__(self, name: str, *songs: tuple or str):
        self.name = name
        self.published = False
        self.songs = [s for s in songs]

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            song_instance = next(filter(lambda s: s.name == song_name, self.songs))

            self.songs.remove(song_instance)

            return f"Removed song {song_name} from album {self.name}."

        except StopIteration:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        info = [f"Album {self.name}"]
        info.extend([f"== {song.get_info()}" for song in self.songs])

        return "\n".join(info)
