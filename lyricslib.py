from urllib.parse import urlparse

def clean_string( s ):
	t = s.strip().replace(' ','').lower()
	return t

def lyrics( artist, song ):
	baseURL = 'www.azlyrics.com/lyrics/'
	cleanedSong = clean_string( song )
	cleanedArtist = clean_string( artist )
	lyricsURL = baseURL + cleanedArtist + '/' + cleanedSong + '.html'
	print( lyricsURL )
