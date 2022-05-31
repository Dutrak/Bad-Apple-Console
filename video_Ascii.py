# pip install to-ascii==3.5.8
# pip install simpleaudio
import toascii
import time
import os
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("video.wav")

v = toascii.Video(
    'video.mp4', scale=0.1, verbose=True)
v.convert()


a = 0
b = len(v.frames)


play_obj = wave_obj.play()
while a < b:
    c = str(v.frames[a])
    print("\033c")
    print(c)
    a += 1
    time.sleep(1/36)
play_obj.wait_done()
