
def clean_string( s , keepSpaces = False):
	if keepSpaces:
		t = s.strip().lower()
	else:
		t = s.strip().replace(' ','').lower()
	return t

def lyrics( artist, song ):
	baseURL = 'http://www.azlyrics.com/lyrics/'
	cleanedSong = clean_string( song )
	cleanedArtist = clean_string( artist )
	lyricsURL = baseURL + cleanedArtist + '/' + cleanedSong + '.html'
	return lyricsURL 

def compare( lyricsFile1, lyricsFile2 ):
	num_target = 0
	num_source = 0
	
	l1 = open( lyricsFile1, 'rU')
	l2 = open( lyricsFile2, 'rU')
	target = clean_string( l1.read(),True )
	source = clean_string( l2.read(),True )
	length = len( source.replace('\n',' ').split(' ') )
	word_counter = [False] * length
	for t in target.replace('\n',' ').split(' '):
		num_source = 0
		for s in source.replace('\n',' ').split(' '):
			if t == s :
				if word_counter[num_source] == False:
					word_counter[num_source] = True
					break
			num_source += 1
		num_target += 1
	return float( sum(word_counter)/num_target ) * 100.0
	
			
