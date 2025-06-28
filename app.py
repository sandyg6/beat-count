from flask import Flask, render_template, request
import numpy as np
import librosa
import io
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def detect_varisai_beats(audio_file, speed, sr=22050):
    y, sr = librosa.load(audio_file, sr=sr)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempogram = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr)
    tempo_multiplier = 1.0
    beat_interval = 1
    if speed == 2:
        tempo_multiplier = 2.0
        beat_interval = 2
    elif speed == 3:
        tempo_multiplier = 4.0
        beat_interval = 3
    beat_frames = np.arange(0, len(onset_env), int(sr * beat_interval / (512 * tempo_multiplier)))
    beats = librosa.frames_to_time(beat_frames, sr=sr, hop_length=512)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return beats, tempo

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['audio_file']
        speed = int(request.form['speed'])
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            beats, tempo = detect_varisai_beats(file_path, speed)
            os.remove(file_path)  # Clean up the uploaded file
            
            # Prepare data to be rendered
            beats_str = [f'{beat:.2f}' for beat in beats]
            num_beats = len(beats)
            
            return render_template('index.html', tempo=tempo, beats_str=beats_str, num_beats=num_beats)
    
    return render_template('index.html', tempo=None, beats_str=None, num_beats=None)

if __name__ == '__main__':
    app.run(debug=True)
