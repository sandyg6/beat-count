# beat-thaalam

## Detecting the number of beats in various speeds of sarali varisai:
[(beat-detection)](https://github.com/sandyg6/beat-thaalam/blob/main/beat.py)
<pre>
<b><i>Objective: </i></b>
    The objective of this application is to detect beats in an uploaded WAV audio file, allowing users to analyse the tempo and rhythm of the music.
  
<b><i>Input Handling: </i></b>
    o Users are prompted to upload a WAV audio file using the file uploader widget provided by Streamlit.
    o They can select the desired speed from a dropdown menu ('1x', '2x', '4x').
    o Users can also input the beat interval value using a number input widget.
  
<b><i>Beat Detection Algorithm: </i></b>
    o	We created a function to implement beat detection algorithm.
    o	It loads the audio file using Librosa, calculates the onset envelope using the function ‘librosa.onset.onset_strength’, and computes the tempogram using ‘librosa.feature.tempogram’.
    o	The tempo multiplier adjusts the beat frames based on the selected speed.
    o	Beat frames are calculated using a numpy array and converted to time using Librosa's ‘frames_to_time’ function.
    o	Finally, the tempo and number of beats are estimated using Librosa's ‘beat_track’ function.
  
<b><i>User Interaction: </i></b>
    o	Users click the 'Detect Beats' button to trigger the beat detection process.
    o	If the audio file is uploaded and the button is clicked, the application displays the tempo, number of beats, and the detected beat times.
  
<b><i>Output Display: </i></b>
    o	The detected tempo in beats per minute (BPM) is shown.
    o	The number of beats detected in the audio file is displayed.
    o	The application provides a list of detected beat times, allowing users to visualize the rhythm and tempo variations.
  
<b><i>Conclusion: </i></b>
    o	This beat detection application provides a user-friendly interface for analyzing the rhythmic characteristics of WAV audio files.
    o	It leverages the capabilities of the Librosa library and Streamlit framework to streamline the process of beat detection and visualization.
    o	Users can easily upload their audio files, adjust parameters, and obtain insights into the tempo and beat structure of their music.
</pre>
