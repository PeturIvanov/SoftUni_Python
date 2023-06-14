def add_songs(*args):
    songs_data = {}
    result = []

    for data in args:
        song_name, song_lyrics = data

        if song_name not in songs_data:
            songs_data[song_name] = []

        if song_lyrics:
            songs_data[song_name].append(song_lyrics)

    for song_name, lyrics in songs_data.items():
        result.append(f"- {song_name}")

        if lyrics:
            result.append('\n'.join(['\n'.join(line) for line in lyrics]))

    return '\n'.join(result)



print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))