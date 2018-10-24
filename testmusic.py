import pygame,sys
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([480,320])
print("播放音乐2")
track1=pygame.mixer.music.load("audio\\01-A.mp3")
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()