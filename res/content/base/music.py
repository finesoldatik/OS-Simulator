from tkinter import *
import fnmatch
import os
from pygame import mixer

from res.api.app import app

class App(app):
  def __init__(self, win, position, args={}):
    self.args = args
    self.muspath = win.system_path + "storage\\Music"
    self.pattern = '*.mp3'
    self.sound = None
    if self.args != {}:
      try:
        self.muspath = args.get("muspath")
      except: pass
    mixer.init()
    self.channel = mixer.find_channel()
    self.music = {}
    super().__init__(win=win, position=position, title="Музыка")
  
  def content(self):
    self.main_frame.config(bg="gray20")

    self.listbox = Listbox(self.main_frame, fg='cyan', bg='gray25', width=50, font=('Consolas', 14))
    self.listbox.pack(padx=15, pady=15)

    self.label = Label(self.main_frame, text='', bg='gray20', fg='yellow', font=('Consolas', 18))
    self.label.pack(pady=15)

    top = Frame(self.main_frame, bg='gray20')
    top.pack(padx=10, pady=5, anchor=CENTER)

    prevBtn = Button(self.main_frame, text='До', width=7, bg='gray23', fg='blue', font=('Consolas', 14), borderwidth=0, command=self.prev)
    prevBtn.pack(pady=15, in_=top, side=LEFT)

    stopBtn = Button(self.main_frame, text='Стоп', width=7, bg='gray23', fg='red', font=('Consolas', 14), borderwidth=0, command=self.stop)
    stopBtn.pack(pady=15, in_=top, side=LEFT)

    playBtn = Button(self.main_frame, text='Выбрать', width=7, bg='gray23', fg='green', font=('Consolas', 14), borderwidth=0, command=self.select)
    playBtn.pack(pady=15, in_=top, side=LEFT)

    self.pauseBtn = Button(self.main_frame, text='Пауза', width=7, bg='gray23', fg='yellow', font=('Consolas', 14), borderwidth=0, command=self.pause)
    self.pauseBtn.pack(pady=15, in_=top, side=LEFT)

    nextBtn = Button(self.main_frame, text='После', width=7, bg='gray23', fg='blue', font=('Consolas', 14), borderwidth=0, command=self.next)
    nextBtn.pack(pady=15, in_=top, side=LEFT)

    volumeFrame = Frame(self.main_frame, bg='gray20')
    volumeFrame.pack(padx=10, pady=5)

    self.volumeScale = Scale(volumeFrame, bg='gray15', fg='white', font=('Consolas', 14), from_=0, to=1, length=374, width=30, resolution=0.1, orient=HORIZONTAL, command=self.volume)
    self.volumeScale.pack(padx=5, pady=5)

    self.listbox.bind('<Double-1>', self.select)

    for root, dirs, files in os.walk(self.muspath):
      for filename in fnmatch.filter(files, self.pattern):
        self.listbox.insert(END, filename)
        self.music[filename] = f"{root}\\{filename}"
  
  def exit(self):
    """Закрывает приложение."""
    self.channel.stop()
    self.win.programslist.delete(self.win.opened_programs.index(self))
    self.win.opened_programs.remove(self)
    self.destroy()

  def select(self, event=None):
    try:
      self.label.configure(text=self.listbox.get(ANCHOR))
      self.sound = mixer.Sound(self.music.get(self.listbox.get(ANCHOR)))
    except:
      self.label.configure(text=self.listbox.get(0))
      self.sound = mixer.Sound(self.music.get(self.listbox.get(0)))

    self.channel.play(self.sound)
    self.channel.set_volume(1)
    self.volumeScale.set(1)
    

  def stop(self):
    self.channel.stop()
    self.listbox.select_clear('active')

  def next(self):
    try:
      next_song = self.listbox.curselection()
      next_song = next_song[0] + 1
      next_song_name = self.listbox.get(next_song)
    except:
      next_song_name = ""

    if next_song_name != "":
      self.label.configure(text=next_song_name)
      self.sound = mixer.Sound(self.music.get(next_song_name))
    else:
      self.label.configure(text=self.listbox.get(0))
      self.sound = mixer.Sound(self.music.get(self.listbox.get(0)))

    self.channel.play(self.sound)
    self.channel.set_volume(1)
    self.volumeScale.set(1)

    self.listbox.select_clear(0, END)
    try:
      self.listbox.activate(next_song)
    except:
      self.listbox.activate(0)
    try:
      self.listbox.select_set(next_song)
    except:
      self.listbox.select_set(0)

  def prev(self):
    try:
      next_song = self.listbox.curselection()
      next_song = next_song[0] - 1
      next_song_name = self.listbox.get(next_song)
    except:
      next_song_name = ""

    if next_song_name != "":
      self.label.configure(text=next_song_name)
      self.sound = mixer.Sound(self.music.get(next_song_name))
    else:
      self.label.configure(text=self.listbox.get(0))
      self.sound = mixer.Sound(self.music.get(self.listbox.get(0)))

    self.channel.play(self.sound)
    self.channel.set_volume(1)
    self.volumeScale.set(1)

    self.listbox.select_clear(0, END)
    try:
      self.listbox.activate(next_song)
    except:
      self.listbox.activate(0)
    try:
      self.listbox.select_set(next_song)
    except:
      self.listbox.select_set(0)
      

  def pause(self):
    if self.pauseBtn["text"] == "Пауза":
      self.channel.pause()
      self.pauseBtn.configure(text='Играть')
    else:
      self.channel.unpause()
      self.pauseBtn.configure(text='Пауза')

  def volume(self, event):
    self.channel.set_volume(self.volumeScale.get())
