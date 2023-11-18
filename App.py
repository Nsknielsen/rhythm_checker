import argparse
from pydub import AudioSegment
import random

def get_file():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()
    return args.file

def get_duration_millis(silence_lower=2000, silence_upper=5000, sound_lower=2000, sound_upper=5000):
    silence_duration = random.randint(silence_lower, silence_upper)
    sound_duration = random.randint(sound_lower, sound_upper)
    return (silence_duration, sound_duration)

def will_not_overflow_track_end(track_length, current_new_track_length, silence_duration_millis, sound_duration_millis):
    next_track_pointer_seconds = current_new_track_length + silence_duration_millis / 1000 + sound_duration_millis / 1000
    return track_length > next_track_pointer_seconds

def with_silence(track):
    start_duration = 4 * 1000
    new_track = track[:start_duration]

    track_pointer = start_duration

    track_length = track.duration_seconds

    silence_duration, sound_duration = get_duration_millis()
    while (will_not_overflow_track_end(track_length, new_track.duration_seconds, silence_duration, sound_duration)):
        silence_segment = AudioSegment.silent(duration=silence_duration)
        new_track += silence_segment
        track_pointer += silence_duration
        sound_segment = track[track_pointer:track_pointer + sound_duration]
        track_pointer += sound_duration
        new_track += sound_segment
        silence_duration, sound_duration = get_duration_millis()

    end = track[track_pointer:]
    new_track += end

    return new_track

if __name__ == "__main__":
    file = get_file()
    track = AudioSegment.from_wav(file)
    new_track = with_silence(track)
    new_track.export("silenced.wav", format="wav")
    print("Generated silences in: ", file)
