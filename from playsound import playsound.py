import pygame
import time

def play_audio():
    file = 'Funny TikTok meme sounds.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"

def alarm(seconds):
    timeelapsed=0
    print(CLEAR)
    while timeelapsed<seconds:
        
        time.sleep(1)
        timeelapsed+=1
        
        timeleft=seconds-timeelapsed
        minutesleft=timeleft//60
        secondsleft=timeleft%60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutesleft:02d}:{secondsleft:02d}")
    play_audio()
    
minutes=int(input("How many minutes to wait: "))
seconds=int(input("How many seconds to wait: "))
total_seconds=minutes*60+seconds
alarm(total_seconds)