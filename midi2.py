from struct import unpack

class Header:
	def __init__(self,type,length,format,tracks,dt):
		self.type = type
		self.length = length
		self.format = format
		self.tracks = tracks
		self.dt = dt

	def __str__(self):
		return str(self.type) + ' ' + str(self.length) + ' ' + str(self.format) + ' ' + str(self.tracks) + ' ' + str(self.dt)

def read_header( filename ):
	file = open(filename,'rb')
	type = file.read(4)
	if type != b'MThd':
		print( "The file entered is not a valid MIDI file")
	length = unpack('>L',file.read(4))[0]
	format = unpack('>H',file.read(2))[0]
	tracks = unpack('>H',file.read(2))[0]
	dt = unpack('>H',file.read(2))[0]
	return Header(type,length,format,tracks,dt)

def read_midi_file( filename ):
	#with open(file,'rb') as inf:
	header=read_header(filename)
	



		
