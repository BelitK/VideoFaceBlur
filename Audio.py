import moviepy.editor
import sys
import os


direts = os.listdir("toBlur")
video_file = sys.argv[1]
# Replace the parameter with the location of the video
# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip(f"{video_file}")
audio = video.audio
# Replace the parameter with the location along with filename
audio.write_audiofile("sample.mp3")