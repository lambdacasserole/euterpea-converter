import sys
import os
import music21


def get_input (path):
    """ Converts a MusicXML file to a list of notes.
    Args:
        path (str): The path of the file to load.
    Returns:
        list of music21.note.Note: A list of all notes in the file at `path`.
    """
    score = music21.converter.parse(path)
    notes = score.flat.notes # Flatten piece, get notes iterator.
    return list(notes) # Using `list` consumes the whole iterator.

def euterpea_name (note):
    """ Returns the Euterpea note name for a music21 note.
    Args:
        note (music21.note.Note): The note to convert.
    Returns:
        str: The Euterpea note name.
    """
    return note.name.lower().replace('#', 's').replace('-', 'f')

def euterpea_len (note):
    """ Returns the Euterpea length name for a music21 note.
    Args:
        note (music21.note.Note): The note to convert.
    Returns:
        str: The Euterpea length name.
    """
    lookup = {
        0.125: 'tn',
        0.1875: 'dtn',
        0.25: 'sn',
        0.375: 'dsn',
        0.5: 'en',
        0.75: 'den',
        1: 'qn',
        1.5: 'dqn',
        2: 'hn',
        3: 'dhn',
        4: 'wn',
        6: 'dwn'
    }
    return lookup.get(note.quarterLength, 'qn') # Quarter note if not found.

def euterpea_constr (note):
    """ Returns the Euterpea note constructor in Haskell for a music21 note.
    Args:
        note (music21.note.Note): The note to convert.
    Returns:
        str: The Euterpea note constructor in Haskell.
    """
    name = euterpea_name(note)
    octave = str(note.octave)
    length = euterpea_len(note)
    return '(' + name + ' ' +  octave + ' ' + length + ')'


# Ensure argument list is correct length.
if len(sys.argv) != 2:
    print("Usage: python toeuterpea.py <input_file>")
    sys.exit()

# Check input file exists.
path = sys.argv[1]
if not os.path.isfile(path):
    print(f"Error: Input file '{path}' does not exist.")
    sys.exit()

# Write out list literal.
print('[', end='')
delim = ''
for note in get_input(path):
    print(delim + euterpea_constr(note), end='')
    delim=', '
print(']')
