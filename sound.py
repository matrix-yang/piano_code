#!/usr/bin/env python

"""extremely simple demonstration playing a soundfile
and waiting for it to finish. you'll need the pygame.mixer
module for this to work. Note how in this simple example we
don't even bother loading all of the pygame package. Just
pick the mixer for sound and time for the delay function.

Optional command line argument:
  the name of an audio file.


"""
import random
import time
import threading
import os.path, sys
import pygame.mixer, pygame.time
mixer = pygame.mixer
pytime = pygame.time

main_dir = os.path.split(os.path.abspath(__file__))[0]

def list_all_files(rootdir="raw\\"):
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def playmusic(path="raw\\a1.ogg"):
    #choose a desired audio format
    mixer.init(11025) #raises exception on fail
    #load the sound
    sound = mixer.Sound(path)
    #start playing
    print ('Playing Sound...'+path)
    channel = sound.play()
    #poll until finished
    while channel.get_busy(): #still playing
        print ('  ...still going...')
        pytime.wait(1000)
    print ('...Finished')


def parse_seq(list):
    index=[]
    interval=[]
    for f in list:
        i=int(f)
        inter=f-i
        index.append(i)
        interval.append(inter)
    return index,interval

def read_file(path="seq\\test.txt"):
    f=open(path, 'r')
    seq=f.read()
    f.close()
    return seq

def write_file(list,path="seq\\test.txt"):
    f=open(path, 'w')
    seq=f.write(list)
    f.close()

def create_random_music(len):
    list1 =[]
    for i in range(len):
        b=random.uniform(1,88)
        list1.append(b)
    return list1

def link_music2thread():
    files=list_all_files()
    threads = []
    for name in files:
        threads.append(threading.Thread(target=playmusic,args=(name,)))
    return threads

def play_list_music(list):
    index,inter=parse_seq(list)
    files=list_all_files()
    for i in range(len(index)):
        print(index[i],inter[i])
        thread=threading.Thread(target=playmusic,args=(files[index[i]],))
        thread.start()
        time.sleep(inter[i])

if __name__ == '__main__':

    list =create_random_music(1222)
    write_file(str(list))

    str1=read_file()
    str2=str1[1:-1]
    print(str2)

    list=str2.split(",")
    list_f=[]
    for s in list:
        list_f.append(float(s))

    print(list_f)
    play_list_music(list_f)
    # threads[1].start()
    #
    # time.sleep(0.3)
    # #t2=threading.Thread(target=playmusic,args=("raw\\b0.ogg",))
    # threads[2].start()
