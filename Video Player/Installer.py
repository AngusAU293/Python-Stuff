import os
import time

install_requierments = '''echo This file will install all module requirements for the player to work
pause
echo Getting pip if not on system...
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo Installing Pygame...
pip install pygame --pre
echo Installing MoviePy
pip install moviepy
echo Succesfully installed modules!
echo Press any key to exit...
pause >nul
'''

readme = '''# Video Player
## **Note: This video player only supports MP4 files**
Stuff around and play videos
'''

play_script = '''import pygame
import moviepy.editor
import glob

video_name_o = glob.glob("Put ONE Video To Play In This Folder\\*.mp4")
video_name = " ".join(map(str, video_name_o))
pygame.init()
video = moviepy.editor.VideoFileClip(video_name)
video.preview()
pygame.quit()
'''
while True:
    def install():
        cd = os.getcwd()
        mainf = os.path.join(cd, "Video Player")

        os.makedirs(mainf)

        md = os.getcwd() + "\Video Player"
        secf = os.path.join(md, "Put ONE Video To Play In This Folder")

        os.makedirs(secf)

        od = os.getcwd() + "\Video Player"
        thif = os.path.join(od, "If Not Working Look In Here")

        os.makedirs(thif)

        print("Creating folders...")
        time.sleep(1)

        with open("Video Player\\Player.py", "w") as play:
            play.write(play_script)
        print("Installing Media Player...")
        time.sleep(2)
        print("Creating README...")
        with open("Video Player\\README.md", "w") as read:
            read.write(readme)
        time.sleep(2)
        print("Creating If Not Working Files...")
        with open("Video Player\\If Not Working Look In Here\\Install Reqirements.bat", "w") as not_working_f:
            not_working_f.write(install_requierments)
        time.sleep(2)
        print("Successfully installed Video Player V-1.0.0")
        input("Press enter to exit: ")
        return True

    def quit():
        return True
    print("Welcome to the Video player V-1.0.0 setup!")
    action = input("Type i to install, or q to quit: ")
    if action == "i":
        install()
    elif action == "q":
        quit()
    else:
        print("Unknown command")
    if quit():
        break
    elif install():
        break
