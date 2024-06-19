from songs import Songs

if Songs.is_empty():
    print("no playable music found")
    exit()
    
    
from tkinter import *
from pygame import mixer
import tkinter.font as font
import random

root = Tk()
root.configure(bg="#252525")
root.geometry('550x250')
root.resizable(0,0)
root.title("musicplayer")
defined_font = font.Font(family='Helvetica')

mixer.init()

class MusicPlayer:
    songpath = Songs.songpath
    songname = Songs.songname
    
    sng = 0
    x = songpath[sng]
    y = songpath.index(x)
    songg = songname[y]

    def playfile(songgpath,songgname):
        MusicPlayer.resetui()
        try:
            print(f'currently playing..\n{songgname}')
            mixer.music.load(songgpath)
            mixer.music.play()
            songtext["text"] = songgname
        except:
            FileNotFoundError
            MusicPlayer.next()

    def play():
        MusicPlayer.playfile(MusicPlayer.x,MusicPlayer.songg)

    def pause():
        mixer.music.pause()
        bt = Button(frm,text="resume",command=MusicPlayer.resume,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
        bt["font"] = defined_font
        bt.grid(row=1,column=1)
        pausedtext.config(text="Paused")

    def resume():
        mixer.music.unpause()
        MusicPlayer.resetui()

    def stopp():
        mixer.music.stop()
        MusicPlayer.resetui()

    def next():
        MusicPlayer.sng += 1
        if MusicPlayer.sng > len(MusicPlayer.songpath)-1:
            MusicPlayer.sng = 0
        MusicPlayer.x = MusicPlayer.songpath[MusicPlayer.sng]
        MusicPlayer.y = MusicPlayer.songpath.index(MusicPlayer.x)
        MusicPlayer.songg = MusicPlayer.songname[MusicPlayer.y]
        songpath = MusicPlayer.x
        songname = MusicPlayer.songg
        MusicPlayer.playfile(songpath,songname)
        MusicPlayer.resetui()

    def prev():
        MusicPlayer.sng -= 1
        if MusicPlayer.sng < 0:
            MusicPlayer.sng = 0
        MusicPlayer.x = MusicPlayer.songpath[MusicPlayer.sng]
        MusicPlayer.y = MusicPlayer.songpath.index(MusicPlayer.x)
        MusicPlayer.songg = MusicPlayer.songname[MusicPlayer.y]
        songpath = MusicPlayer.x
        songname = MusicPlayer.songg
        MusicPlayer.playfile(songpath,songname)
        MusicPlayer.resetui()

    def randomsong():
        songpath = random.choice(MusicPlayer.songpath)
        songname2 = MusicPlayer.songpath.index(songpath)
        songname = MusicPlayer.songname[songname2]
        MusicPlayer.sng = songname2
        MusicPlayer.playfile(songpath,songname)
        MusicPlayer.resetui()

    def resetui():
        bt = Button(frm,text="pause",command=MusicPlayer.pause,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
        bt["font"] = defined_font
        bt.grid(row=1,column=1)
        pausedtext.config(text="")

my_menu = Menu(root,bg="#252525")
my_menu.add_cascade(label=f'SONGS  ({len(MusicPlayer.songname)})',font=defined_font,)

musicfrm = Frame(root,bg="#252525")
musicfrm.pack(padx=10,pady=10)

songtext = Label(musicfrm,text="song name",width=60,height=4,background="#252525",fg="#fff",font=(defined_font,20))
songtext.pack()

frm = Frame(root,bg="#252525")
frm.pack(padx=10,pady=10)

bt = Button(frm,text="play",command=MusicPlayer.play,width=10,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt["font"] = defined_font
bt.grid(row=1,column=2)

bt1 = Button(frm,text="pause",command=MusicPlayer.pause,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt1["font"] = defined_font
bt1.grid(row=1,column=1)

bt2 = Button(frm,text="stop",command=MusicPlayer.stopp,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt2["font"] = defined_font
bt2.grid(row=1,column=3)

bt3 = Button(frm,text="next",command=MusicPlayer.next,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt3["font"] = defined_font
bt3.grid(row=1,column=4)

bt4 = Button(frm,text="previous",command=MusicPlayer.prev,width=8,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt4["font"] = defined_font
bt4.grid(row=1,column=0)

pausedtext = Label(frm,text="",width=5,background="#252525",fg="red",font=(defined_font,18),)
pausedtext.grid(row=2,column=1)

bt = Button(frm,text="random",command=MusicPlayer.randomsong,width=10,bg="#b0a9ac",fg="#050204",activebackground="#52a9b3")
bt["font"] = defined_font
bt.grid(row=2,column=2)

root.configure(menu=my_menu)
root.mainloop()            