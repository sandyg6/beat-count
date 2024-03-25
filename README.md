# beat-thaalam

## Detecting the number of beats in various speeds of sarali varisai:
[(beat-detection)](https://github.com/sandyg6/beat-thaalam/blob/main/beat.py)

<b><i>Objective: </i></b>
    The objective of this application is to detect beats in an uploaded WAV audio file, allowing users to analyse the tempo and rhythm of the music.
  
<b><i>Input Handling: </i></b>
<ul>
    <li>Users are prompted to upload a WAV audio file using the file uploader widget provided by Streamlit.</li>
    <li>They can select the desired speed from a dropdown menu ('1x', '2x', '4x').</li>
    <li>Users can also input the beat interval value using a number input widget.</li>
</ul>
  
<b><i>Beat Detection Algorithm: </i></b>
<ul>
    <li>We created a function to implement beat detection algorithm.</li>
    <li>It loads the audio file using Librosa, calculates the onset envelope using the function ‘librosa.onset.onset_strength’, and computes the tempogram using ‘librosa.feature.tempogram’.</li>
   <li>The tempo multiplier adjusts the beat frames based on the selected speed.</li>
   <li>Beat frames are calculated using a numpy array and converted to time using Librosa's ‘frames_to_time’ function.</li>
   <li>Finally, the tempo and number of beats are estimated using Librosa's ‘beat_track’ function.</li>
    </ul>
  
<b><i>User Interaction: </i></b>
    <ul>
    <li>Users click the 'Detect Beats' button to trigger the beat detection process.</li>
    <li>If the audio file is uploaded and the button is clicked, the application displays the tempo, number of beats, and the detected beat times.</li>
    </ul>
  
<b><i>Output Display: </i></b>
<ul>
<li>The detected tempo in beats per minute (BPM) is shown.</li>
<li>The number of beats detected in the audio file is displayed.</li>
<li>The application provides a list of detected beat times, allowing users to visualize the rhythm and tempo variations.</li>
</ul>

<b><i>Conclusion: </i></b>
<ul>
    <li>This beat detection application provides a user-friendly interface for analyzing the rhythmic characteristics of WAV audio files.</li>
  <li>It leverages the capabilities of the Librosa library and Streamlit framework to streamline the process of beat detection and visualization.</li>
 <li>Users can easily upload their audio files, adjust parameters, and obtain insights into the tempo and beat structure of their music.</li>
</ul>
  

