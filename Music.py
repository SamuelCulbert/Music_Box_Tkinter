from tkinter import *
from pygame import mixer
from tkinter import filedialog
import os
def prev_song():
    next_s = song_box.curselection()
    next_s = next_s[0] - 1
    song = song_box.get(next_s)
    song = mapsong[song]
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)
def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    song = mapsong[song]
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)
def play_song():
    song = song_box.get(ACTIVE)
    song = mapsong[song]
    mixer.music.load(song)
    mixer.music.play()
    song_state['text'] = "Playback"
def stop_song():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Paused"
def pause_song():
    if song_state['text'] == "Pause":
        mixer.music.unpause()
        song_state['text'] = "Playing"

    else:
        mixer.music.pause()
        song_state['text'] = "Pause"
def OpenFile():
    
    song = filedialog.askopenfilename(initialdir='tracks/', title="Choose a song!", filetypes=(("mp3 Files", "*.mp3"),))
    
    filename = os.path.basename(song)
    mapsong[filename] = song
    song_box.insert(END, filename)
    
def OpenFolder():
    songs = filedialog.askopenfilenames(initialdir='tracks/', title="Choose a song!", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        filename = os.path.basename(song)
        mapsong[filename] = song
        song_box.insert(END, filename)
mixer.init()
root = Tk()
mapsong = {}
master_frame = Frame(root)
master_frame.pack()
info_frame = Frame(master_frame)
info_frame.grid(row=0, column=0)
song_state = Label(info_frame, width=50, text="Paused", font="Arial 8 bold", fg="Brown")

song_state.grid(row=0, column=0)
song_box = Listbox(info_frame, width=50, selectbackground="Blue")
song_box.grid(row=1, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)
back_button = Button(controls_frame, text="⏪︎", width=6, command=prev_song)
back_button.grid(row=0, column=0)
nextButton = Button(controls_frame, text="⏩︎", width=6, command=next_song)
nextButton.grid(row=0, column=1)
playButton = Button(controls_frame, text="play ▶", width=6, command=play_song, fg="Green")
playButton.grid(row=1, column=0)
pausebutton = Button(controls_frame, text="pause ⏸", width=6, command=pause_song)
pausebutton.grid(row=1, column=1)
StopButton = Button(controls_frame, text="stop ⏹︎", width=6, command=stop_song, fg="Red")
StopButton.grid(row=1, column=2)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)
openFile = Button(file_frame, text="OpenFile", width=12, command=OpenFile)
openFile.grid(row=0, column=0)
openFolder = Button(file_frame, text="OpenMultipleFIle", width=15, command=OpenFolder)
openFolder.grid(row=1, column=0)



root.mainloop()
