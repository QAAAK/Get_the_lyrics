# pip install lyricsgenius
import lyricsgenius
api_key = "xxxxxxxxxxxxxxxxxxxxx"
genius = lyricsgenius.Genius(api_key)

artist_get = str(input('Enter the artist: '))
artist = genius.search_artist(artist_get,
max_songs=5,sort="title")

song_get = str(input('Enter the song: '))
song = artist.song(song_get)
print(song.lyrics)
