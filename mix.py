import moviepy.editor as mp
import os


diretvid = os.listdir("toBlur")
diretsound = os.listdir("sounds")
#os.mkdir("finished")
for video in diretvid:

    clip = mp.VideoFileClip(f"blurred/{video[:-4]}.mp4")
    print(video)
    audioclip = mp.VideoFileClip(f"toBlur/{video}")
    #print(f"sounds/{video[:-4]}.mp3")
    #fVid = mp.CompositeAudioClip([clip.audio,audioclip])
    finalclip = clip.set_audio(audioclip.audio)
    finalclip.write_videofile(f"finished/{video[:-4]}.mp4")
