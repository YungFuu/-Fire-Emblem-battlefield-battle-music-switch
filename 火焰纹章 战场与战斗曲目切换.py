# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:00:16 2022

@author: hp
"""
import difflib
import time,os,random
import pygame
from datetime import datetime as dt
import eyed3




path = r'C:\Users\hp\Music'
song_list=[]



def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
def get_key (dict, value):
               return [k for k, v in dict.items() if v == value]



for i in os.listdir(path):
    if ".mp3" in i:
        song_list.append(i)

song_dict={}
for z in range(0,6):
    for i in song_list:
        if ' - Battle On ' in i:
            i_changed = i.split('- Battle On')[1]
            i_changed = i_changed.split('(')[1]
            i_changed = i_changed.split(')')[0]
            for j in song_list:
                if i == j :
                    pass
                elif i_changed in j:
                    song_dict[j]=i
                    song_list.remove(i)
                    song_list.remove(j)
                
                    
        else:
            for j in song_list:
                if string_similar(i, j) > 0.9:     
                    if len(i) < len(j):
                        song_dict[i]=j
                    else:
                        song_dict[j]=i
                else:
                    pass

print(song_dict)
#%%
pygame.mixer.init()
song_list =  list(song_dict.keys())
#song_list = list(map(lambda x: path + os.sep + x,song_list))
file = song_list[random.randint(0, len(song_list)-1)]

def play(file=file):
    global begin_point
    file_path = path + os.sep + file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    begin_point = dt.now()
    print('正在播放',file)
    
def change_type():
    global file
    #歌曲已经播放了多少秒
    change_point = dt.now()
    new_begin_time = change_point-begin_point
    pygame.mixer.music.stop()
    
    if file not in song_dict.keys():
        file = get_key(song_dict,file)[0]
    else:
        file = song_dict[file]
    
    file_path = path + os.sep + file
    pygame.mixer.music.load(file_path)
    
    #从歌曲已经播放了秒数位置开始播放
    pygame.mixer.music.play(start=new_begin_time.seconds)
    print('正在播放',file)
    print(new_begin_time)
    
def random_song():
    global file
    file = song_list[random.randint(0, len(song_list)-1)]
    play(file)
    
# play()


def auto_play():
    for song in song_list:
        mp3Info = eyed3.load(path+os.sep+song)
        play(song)
        time.sleep(mp3Info.info.time_secs)
        
def auto_changed():
    random_song()
    for i in range(random.randint(4, 6)):
        time.sleep(random.randint(10, 20))
        change_type()
        
def auto_playchange():
        for a in range(len(song_list)):
            random_song()
            for i in range(random.randint(4, 6)):
                time.sleep(random.randint(10, 20))
                change_type()
