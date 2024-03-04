from tkinter import *
import fnmatch
import os
from pygame import mixer

from res.modules.app import app

class App(app):
  def __init__(self, win, position, args=[]):
    super().__init__(win=win, position=position, title="Музыка")
    self.args = args
    self.config(bg="gray20")
    if self.args == []:
      self.muspath = win.system_path + "storage\\Music"
    else:
      self.muspath = args[0]
    self.pattern = '*.mp3'

    mixer.init()
    
  def select(self, event=None):
    self.label.configure(text=self.listbox.get(ANCHOR))
    mixer.music.load(f"{self.muspath}\\{self.listbox.get(ANCHOR)}")
    mixer.music.play()
    mixer.music.set_volume(1)
    self.volumeScale.set(1)

  def stop(self):
    mixer.music.stop()
    self.listbox.select_clear('active')

  def next(self):
    next_song = self.listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = self.listbox.get(next_song)
    self.label.configure(text=next_song_name)

    mixer.music.load(f"{self.muspath}\\{next_song_name}")
    mixer.music.play()
    mixer.music.set_volume(1)
    self.volumeScale.set(1)

    self.listbox.select_clear(0, END)
    self.listbox.activate(next_song)
    self.listbox.select_set(next_song)

  def prev(self):
    next_song = self.listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name = self.listbox.get(next_song)
    self.label.configure(text=next_song_name)

    mixer.music.load(f"{self.muspath}\\{next_song_name}")
    mixer.music.play()
    mixer.music.set_volume(1)
    self.volumeScale.set(1)

    self.listbox.select_clear(0, END)
    self.listbox.activate(next_song)
    self.listbox.select_set(next_song)

  def pause(self):
    if self.pauseBtn["text"] == "Пауза":
      mixer.music.pause()
      self.pauseBtn.configure(text='Играть')
    else:
      mixer.music.unpause()
      self.pauseBtn.configure(text='Пауза')

  def volume(self, event):
    mixer.music.set_volume(self.volumeScale.get())

  def main(self):
    self.listbox = Listbox(self, fg='cyan', bg='gray25', width=100, font=('Consolas', 14))
    self.listbox.pack(padx=15, pady=15)

    self.label = Label(self, text='', bg='gray20', fg='yellow', font=('Consolas', 18))
    self.label.pack(pady=15)

    self.top = Frame(self, bg='gray20')
    self.top.pack(padx=10, pady=5, anchor=CENTER)

    self.prevBtn = Button(self, text='До', width=7, bg='gray23', fg='blue', font=('Consolas', 14), borderwidth=0, command=self.prev)
    self.prevBtn.pack(pady=15, in_=self.top, side=LEFT)

    self.stopBtn = Button(self, text='Стоп', width=7, bg='gray23', fg='red', font=('Consolas', 14), borderwidth=0, command=self.stop)
    self.stopBtn.pack(pady=15, in_=self.top, side=LEFT)

    self.playBtn = Button(self, text='Выбрать', width=7, bg='gray23', fg='green', font=('Consolas', 14), borderwidth=0, command=self.select)
    self.playBtn.pack(pady=15, in_=self.top, side=LEFT)

    self.pauseBtn = Button(self, text='Пауза', width=7, bg='gray23', fg='yellow', font=('Consolas', 14), borderwidth=0, command=self.pause)
    self.pauseBtn.pack(pady=15, in_=self.top, side=LEFT)

    self.nextBtn = Button(self, text='После', width=7, bg='gray23', fg='blue', font=('Consolas', 14), borderwidth=0, command=next)
    self.nextBtn.pack(pady=15, in_=self.top, side=LEFT)

    self.volumeFrame = Frame(self, bg='gray20')
    self.volumeFrame.pack(padx=10, pady=5)

    self.volumeScale = Scale(self.volumeFrame, bg='gray15', fg='white', font=('Consolas', 14), from_=0, to=1, length=374, width=30, resolution=0.1, orient=HORIZONTAL, command=self.volume)
    self.volumeScale.pack(padx=5, pady=5)

    self.listbox.bind('<Double-1>', self.select)

    for rootf, dirs, files in os.walk(self.muspath):
      for filename in fnmatch.filter(files, self.pattern):
        self.listbox.insert(END, filename)
