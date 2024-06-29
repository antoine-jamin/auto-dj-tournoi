# -*-coding:Latin-1 -*
__author__ = "Antoine JAMIN"

# Librairies

import appscript
import subprocess
from tkinter import *
import time

# Variables globales
bgcolor = 'white' # couleur de fond
sonDebut = "debutdematch.mp3" # musique de début de match
sonFin = "findematch.mp3"     # musique de fin de match
tempsFin = 50.0 # Durée de la musique de fin
volume="0.7"

application_musique = "Spotify" # "iTunes" ou "Spotify"
#application_musique = "iTunes"
appMusic = appscript.app(application_musique)




# Fonctions
def Start():
    PlayMusicDeb()
    temps = float(SboxMin.get())*60+float(SboxSec.get())
    #Enlève le temps de fin
    temps=temps-tempsFin
    print('Il reste ' + str(int(temps/60)) + '\'' +str(int(temps%60))+'\'\' avant la musique de fin')
    while(temps!=0):
        time.sleep(1)
        temps=temps-1
        print('Il reste ' + str(int(temps / 60)) + '\'' + str(int(temps % 60)) + '\'\' avant la musique de fin')
    PlayMusicFin()
    print("----------- END -----------\n")

def SpaceStart(event):
    Start()

def Play():
    if appMusic.isrunning():
        appMusic.play()

def Pause():
    if appMusic.isrunning():
        appMusic.pause()

def PlayMusicDeb():
    print("\nMusique de début\n")
    Pause()
    subprocess.call(["afplay", sonDebut, "-v", volume])
    Play()

def KeyPlayMusicDeb(event):
    PlayMusicDeb()

def PlayMusicFin():
    print("\nMusique de fin\n")
    Pause()
    subprocess.call(["afplay", sonFin, "-v", volume])
    Play()

def KeyPlayMusicFin(event):
    PlayMusicFin()

def KeyNextMusic(event):
    if appMusic.isrunning():
        appMusic.next_track()

def KeyPlay(event):
    Play()

def KeyPause(event):
    Pause()

# Partie Graphique
if __name__ == "__main__":
    win = Tk()
    win.title("Auto-Dj")
    title = Label(win, text="Auto-Dj",font=("", 40), fg="blue", bg=bgcolor)
    title.pack(pady=10)
    txt = Label(win, text="Durée des matchs :", font=("", 26), bg=bgcolor)
    txt.pack(pady=2)
    frame1=Frame(win, bg=bgcolor)
    frame1.pack(pady=1)
    txt1 = Label(frame1, text="Minutes : ", font=("", 20), bg=bgcolor)
    txt1.pack(side=LEFT)
    SboxMin = Spinbox(frame1, from_=1, to=60, increment=1, bg=bgcolor, width=3)
    SboxMin.pack(side=RIGHT)
    frame2 = Frame(win, bg=bgcolor)
    frame2.pack(pady=1)
    txt2 = Label(frame2, text="Secondes : ", font=("", 20), bg=bgcolor)
    txt2.pack(side=LEFT)
    SboxSec = Spinbox(frame2, from_=0, to=45, increment=15, bg=bgcolor, width=3)
    SboxSec.pack(side=RIGHT)

    frame3 = Frame(win, bg=bgcolor)
    frame3.pack(pady=20)

    Button(frame3, text="Start", command=Start).pack(side=LEFT, padx=10)
    Button(frame3, text="Musique de début", command=PlayMusicDeb).pack(side=LEFT, padx=10)
    Button(frame3, text="Musique de fin", command=PlayMusicFin).pack(side=LEFT, padx=10)

    frame4 = Frame(win, bg=bgcolor)
    frame4.pack(pady=2)
    Label(frame4, text="------").pack(pady=10)
    Label(frame4, text="espace : START | ").pack(side=LEFT,pady=2)
    Label(frame4, text="F1 : Musique de début | ").pack(side=LEFT,pady=2)
    Label(frame4,text="F10 : Musique de fin | ").pack(side=LEFT,pady=2)
    Label(frame4,text="Entrée : Chanson suivante").pack(side=LEFT,pady=2)

    frame5 = Frame(win, bg=bgcolor)
    frame5.pack(pady=2)
    Label(frame5, text="a : Play | ").pack(side=LEFT, pady=2)
    Label(frame5, text="o : Pause").pack(side=LEFT, pady=2)

    attente= Entry(win)
    attente.insert(0,"zone d'attente curseur")
    attente.pack(pady=2)

    win.bind("<space>", SpaceStart)
    win.bind("<F1>",KeyPlayMusicDeb)
    win.bind("<F10>",KeyPlayMusicFin)
    win.bind("<Return>",KeyNextMusic)
    win.bind("a", KeyPlay)
    win.bind("o", KeyPause)


    win.mainloop()

