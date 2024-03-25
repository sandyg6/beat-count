#importing the libraries
import streamlit as st
import numpy as np
import librosa
import librosa.display

#Creating a function for detecting the number of beats in the given audio file using librosa's onset_strength functions, feature.tempogram functions, frames_to_time functions and beat_track functions
def detect_varisai_beats(audio_file, speed, beat_interval, sr=22050):
    y, sr = librosa.load(audio_file, sr=sr)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempogram = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr)
    tempo_multiplier = 1.0
    if speed == 2:
        tempo_multiplier = 2.0
    elif speed == 3:
        tempo_multiplier = 4.0
    beat_frames = np.arange(0, len(onset_env), int(sr * beat_interval / (512 * tempo_multiplier)))
    beats = librosa.frames_to_time(beat_frames, sr=sr, hop_length=512)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return beats, tempo

#Creating a frontend using streamlit 
def main():
    st.title('Beat Detection App')
    # Get user inputs
    audio_file = st.file_uploader('Upload WAV File', type=['wav'])
    speed = st.selectbox('Select Speed', ['1x', '2x', '4x'])
    beat_interval = st.number_input('Enter Beat Interval', value=512)

    # Convert speed to multiplier
    speed_multipliers = {'1x': 1, '2x': 2, '4x': 4}
    speed_multiplier = speed_multipliers[speed]

    # Submit button
    if st.button('Detect Beats') and audio_file is not None:
        beats, tempo = detect_varisai_beats(audio_file, speed_multiplier, beat_interval)
        st.write(f'Tempo: {tempo} BPM')
        st.write(f'Number of Beats: {len(beats)}')
        st.write('Detected Beats:')
        st.write(beats)

if __name__ == '__main__':
    main()
