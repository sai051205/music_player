from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class Music:
    def __init__(self, root):
        # Create Tkinter window
        root.geometry('400x400')
        root.title('MP3 MUSIC PLAYER')
        root.resizable(0, 0)
        root.configure(background='#999999')


        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('PLAY')
        self.pause_resume.set('PAUSE')

        # The buttons and their positions
        load_button = Button(root, text='LOAD', width=10, font=('times new roman', 15), command=self.load)
        load_button.place(x=200, y=40, anchor='center')

        play_button = Button(root, textvariable=self.play_restart, width=10, font=('times new roman',15), command=self.play)
        play_button.place(x=200, y=80, anchor='center')

        pause_button = Button(root, textvariable=self.pause_resume, width=10, font=('times ew roman', 15), command=self.pause)
        pause_button.place(x=200, y=120, anchor='center')

        stop_button = Button(root, text='STOP', width=10, font=('times new roman', 15), command=self.stop)
        stop_button.place(x=200, y=160, anchor='center')

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()


root = Tk()
Music(root)
root.mainloop()