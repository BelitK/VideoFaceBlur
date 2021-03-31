from moviepy.editor import *
import os


# direts = os.listdir("blurred")
# for name in direts:
#
#
#
# # loading video dsa gfg intro video
#     clip = VideoFileClip(f"blurred/{name}")
#
# # loading audio file
#     print(f"sounds/{name[:-4]}.mp3")
#     audioclip = AudioFileClip(f"sounds/{name[:-4]}.mp3")
#
# # adding audio to the video clip
#     videoclip = clip.set_audio(audioclip)
#
#     clip.write_videofile(f"{name}")
clip = VideoFileClip(f"blurred/{name}")