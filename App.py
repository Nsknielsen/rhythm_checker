import argparse
from pydub import AudioSegment

def get_file():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()
    return args.file

if __name__ == "__main__":
    file = get_file()
    
    track = AudioSegment.from_wav(file)

    start_duration = 3 * 1000
    before_silence = track[:start_duration]

    silence_duration = 2 * 1000
    silence = AudioSegment.silent(duration=silence_duration)

    after_silence = track[start_duration + silence_duration:]

    new_track = before_silence + silence + after_silence
    new_track.export("silenced.wav", format="wav")
    print("Generated 2 seconds of silence at seconds 3-5 of file: ", file)
