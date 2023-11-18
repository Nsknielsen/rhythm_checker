## Getting started
This is a command-line program that requires an argument with a path to a WAV file. 
The program selects random 2-5 second sequences of this WAV file that are replaced with silence in an output file.

Usecases:
- For practicing tempo as a musician. Add silences to a recording and play along with it, making sure to keep tempo during the silenced parts of the track.

### Prerequisites
Python 3 and `pip` or a similar package manager.

### Usage
1. Clone this repository.
2. From the root folder, install dependencies eg. with `pip install -r requirements.txt`.
3. Run the program with `python App.py --file [absolutePathToYourWavFile] [optionalArguments]`
4. The output file is found in the root folder as `silenced-[inputFileName].wav`

### Arguments
- `-f | --file`: The .wav file that you want to add silences to.
- `--silence_lower` (optional): Lower bound for the duration of each silence segment in milliseconds.
- `--silence_upper` (optional): Upper bound for the duration of each silence segment in milliseconds.
- `--sound_lower` (optional): Lower bound for the duration of each sound segment in milliseconds.
- `--sound_upper` (optional): Upper bound for the duration of each sound segment in milliseconds.

<b>Example usage:</b> `python App.py --file "C:\Users\nsknielsen\desktop\aalborg_polka.wav" --silence_lower 3000 --silence_upper 6000`

## License
[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.txt)