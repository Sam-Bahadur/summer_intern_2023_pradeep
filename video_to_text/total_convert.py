import moviepy.editor as mp
import speech_recognition as sr
from tkinter.filedialog import *
import csv


# Convert video to audio
def convert_video_to_audio(video_path, audio_path):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

# Transcribe audio to text
def transcribe_audio(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        return text

# Main function
def main():
    video_path = askopenfilename()
    audio_path = "test_audio_converted.wav"
    output_csv_path = "output.csv"
    
    # Convert video to audio
    convert_video_to_audio(video_path, audio_path)

    # Transcribe audio to text
    print("working on it....")
    transcribed_text = transcribe_audio(audio_path)
    
    print("Transcribed text:")
    print(transcribed_text)

    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        writer.writerow([transcribed_text])

if __name__ == "__main__":
    main()
