from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('430x50'); window.title('Welcome'); window.resizable(0,0); window.configure(bg="black");
        Load = Button(window, text = 'Load',  width = 12, font = ('Helvetica', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 12,font = ('Helvetica', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 12, font = ('Helvetica', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 12, font = ('Helvetica', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=330,y=20)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
