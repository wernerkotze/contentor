import lyricsgenius

def get_song_lyrics(artist, track):

	lyrics = get_song_lyrics(artist, track)
	if not lyrics:
		return False

	has_chorus = False
	if isinstance(lyrics, list):
		for lyric in lyrics:
			pattern = '[Chorus'
			chorus  = lyric.find(pattern)
			print(chorus)
			if chorus == -1:
				return False
			else:
				has_chorus = True
	else:
		pattern = '[Chorus'
		chorus  = lyrics.find(pattern)
		print(chorus)
		if chorus == -1:
			return False
		else:
			has_chorus = True

	if not has_chorus:
		return False

def find_lyric_pattern(pattern):
	chorus  = lyric.find(pattern)
	print(chorus)
	if chorus == -1:
		return False
	else:
		has_chorus = True

