def strip_audio(targetAud,pathVid):
    """pathAud for writing audio file path and pathVid for getting video file paths"""
    import os
    import moviepy.editor as mp
    if os.path.isdir(targetAud) is False:
        print("file doesn`t exist so creating export file")
        os.mkdir(targetAud)
    else:
        pass
    direts = os.listdir(f"{pathVid}")
    for tst in direts:
        video_file = f"{pathVid}/{tst}"
        print(video_file)

        video = mp.VideoFileClip(video_file)
        audio = video.audio

        #change format to ffmpeg of your choice

        audio.write_audiofile(f"{targetAud}/{tst[:-4]}.mp3")

def mixAuVid(pathAud,pathVid,pathTarget):
    """pathAud for audio file paths, pathVid for video file paths and pathTarget for finished work to be put"""
    import os
    import moviepy.editor as mp
    if os.path.isdir(pathTarget) is False:
        print("target file doesn`t exist so creating export file")
        os.mkdir(pathTarget)
    else:
        pass
    diretvid = os.listdir(pathVid)
    diretsound = os.listdir(pathAud)
    for video in diretvid:
        clip = mp.VideoFileClip(f"{pathVid}/{video[:-4]}.mp4")
        print(video)
        audioclip = mp.AudioFileClip(f"{pathAud}/{video[:-4]}.mp3")
        finalclip = clip.set_audio(audioclip)
        finalclip.write_videofile(f"{pathTarget}/{video[:-4]}.mp4")



