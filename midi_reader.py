import midi
import numpy as np

def normalize(duration,resolution):
	if duration == resolution*4:
		return 64
	elif duration == resolution*3:
		return 48
	elif duration == resolution*2:
		return 32
	elif duration == resolution*1.5:
		return 24
	elif duration == resolution:
		return 16
	elif duration == resolution*3/4:
		return 12
	elif duration == resolution/2:
		return 8
	elif duration == resolution*3/8:
		return 6
	elif duration == resolution/4:
		return 4
	elif duration == resolution/8:
		return 2
	elif duration == resolution/16:
		return 1
	else:
		return 0

def read_midi( filename ):
	pattern = midi.read_midifile( filename )
	notes = []
	note_onsets = {}
	for track in pattern:
		note_events = [e for e in track if isinstance(e, midi.NoteEvent)]
		tick = 0
		for e in note_events:
			is_note_on = isinstance(e, midi.NoteOnEvent)
			is_note_off = isinstance(e, midi.NoteOffEvent)
			
			if is_note_on and e.velocity > 0:
				note_onsets[e.pitch] = e.tick
				
			elif is_note_off or (is_note_on and e.velocity == 0):
				notes.append((e.pitch, normalize(e.tick - note_onsets[e.pitch],pattern.resolution)))
				
			tick = e.tick
	notes = np.asarray(notes)
	return notes