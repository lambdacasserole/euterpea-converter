# Euterpea Converter
Converts MusicXML files to Euterpea Haskell code.

## Overview

This Python script converts MusicXML files into a list of notes formatted for Euterpea, a Haskell library for computer music. The script reads a MusicXML file, extracts the musical notes, and outputs them as Euterpea note constructors in Haskell syntax. This utility is particularly useful for musicians and computer music researchers looking to bridge the gap between MusicXML notation and Euterpea's powerful music composition and analysis capabilities.

## Features

- **MusicXML Parsing**: Load and parse MusicXML files to extract musical notes.
- **Note Conversion**: Convert music21 note objects to Euterpea note names and lengths.
- **Euterpea Constructor Generation**: Generate Euterpea note constructors in Haskell, supporting both individual notes and chords.

## Requirements

- Python 3.x
- `music21` library for parsing MusicXML files. Install it using pip:
  ```
  pip install music21
  ```

## Usage

1. Ensure you have Python and `music21` installed on your system.
2. Save the script to a file, e.g., `toeuterpea.py`.
3. Run the script from the command line, specifying the path to your MusicXML file as an argument:

   ```
   python toeuterpea.py <input_file>
   ```

   Replace `<input_file>` with the path to your MusicXML file.

4. The script will output the list of notes in Euterpea format to the console.

## Example

Given a MusicXML file named `example.xml`, run:

```
python toeuterpea.py example.xml
```

Output (example):

```
[(c 4 qn), (e 4 qn), (g 4 qn), (c 5 hn)]
```

This represents a sequence of quarter notes C, E, G in the 4th octave, followed by a half note C in the 5th octave, formatted for Euterpea.

## Function Descriptions

- `get_input(path)`: Converts a MusicXML file to a list of notes.
- `euterpea_name(note)`: Returns the Euterpea note name for a given note.
- `euterpea_len(note)`: Returns the Euterpea length name for a given note.
- `euterpea_constr(note)`: Returns the Euterpea note constructor in Haskell for a given note or chord.

## Contributions

Contributions to improve or extend the functionality of this script are welcome. Please feel free to fork the project, make your changes, and submit a pull request.

## License

This script is released under the MIT License. See the LICENSE file for more details.
