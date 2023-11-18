import argparse
from pydub import AudioSegment
import random
import os

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', '--file')
    arg_parser.add_argument('--silence_lower', default=2000)
    arg_parser.add_argument('--silence_upper', default=5000)
    arg_parser.add_argument('--sound_lower', default=2000)
    arg_parser.add_argument('--sound_upper', default=5000)
    return arg_parser.parse_args()

def get_duration_millis(silence_lower, silence_upper, sound_lower, sound_upper):
    silence_duration = random.randint(silence_lower, silence_upper)
    sound_duration = random.randint(sound_lower, sound_upper)
    return (silence_duration, sound_duration)

def will_not_overflow_track_end(track_length_seconds, current_new_track_length, silence_duration_millis, sound_duration_millis):
    next_track_pointer_seconds = current_new_track_length + silence_duration_millis / 1000 + sound_duration_millis / 1000
    return track_length_seconds > next_track_pointer_seconds

def with_silences(track, silence_lower, silence_upper, sound_lower, sound_upper):
    start_duration = 4 * 1000
    new_track = track[:start_duration]

    track_pointer = start_duration

    track_length = track.duration_seconds

    silence_duration, sound_duration = get_duration_millis(silence_lower, silence_upper, sound_lower, sound_upper)
    while (will_not_overflow_track_end(track_length, new_track.duration_seconds, silence_duration, sound_duration)):
        silence_segment = AudioSegment.silent(duration=silence_duration)
        new_track += silence_segment
        track_pointer += silence_duration
        sound_segment = track[track_pointer:track_pointer + sound_duration]
        track_pointer += sound_duration
        new_track += sound_segment
        silence_duration, sound_duration = get_duration_millis(silence_lower, silence_upper, sound_lower, sound_upper)

    end = track[track_pointer:]
    new_track += end

    return new_track

if __name__ == "__main__":
    args = get_args()
    file = args.file
    track = AudioSegment.from_wav(file)
    silence_lower = args.silence_lower
    silence_upper = args.silence_upper
    sound_lower = args.sound_lower
    sound_upper = args.sound_upper
    new_track = with_silences(track, silence_lower, silence_upper, sound_lower, sound_upper)

    old_filename = os.path.basename(os.path.normpath(file))
    new_filename = f'silenced-{old_filename}.wav'
    new_track.export(new_filename, format="wav")
    print("Generated silences for: ", file)
