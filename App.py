import argparse
from pydub import AudioSegment
import random

def get_file():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()
    return args.file

def get_durations(silence_lower=2, silence_upper=5, sound_lower=2, sound_upper=5):
    silence_duration = random.randint(silence_lower, silence_upper) * 1000
    sound_duration = random.randint(sound_lower, sound_upper) * 1000
    return (silence_duration, sound_duration)

def with_silence(track):
    start_duration = 4 * 1000
    start = track[:start_duration]

    new_track_segments = [start]
    track_pointer = start_duration

  
    for i in range(5):
        silence_duration, sound_duration = get_durations()
        silence_segment = AudioSegment.silent(duration=silence_duration)
        new_track_segments.append(silence_segment)
        track_pointer += silence_duration
        sound_segment = track[track_pointer:track_pointer + sound_duration]
        track_pointer += sound_duration
        new_track_segments.append(sound_segment)

    end = track[track_pointer:]
    new_track_segments.append(end)

    new_track = AudioSegment.empty()
    for i in range(len(new_track_segments)):
        new_track += new_track_segments[i]

    return new_track

if __name__ == "__main__":
    file = get_file()
    track = AudioSegment.from_wav(file)
    new_track = with_silence(track)
    new_track.export("silenced.wav", format="wav")
    print("Generated silences in: ", file)
