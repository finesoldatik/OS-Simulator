from tkinter import *
import tkVideoPlayer as vp

from res.api.app import app

class App(app):
  def __init__(self, win, position, args={}):
    self.args = args
    if self.args == []:
      self.video = win.system_path + "storage\\Video\\1.mp4"
    else:
      self.video = args[0]
    super().__init__(win=win, position=position, title="Видео")

  def play(self):
    self.videoplayer.play()

  def pause(self):
    self.videoplayer.pause()

  def stop(self):
    self.videoplayer.stop()

  def main(self):
    self.main_frame.config(bg="gray20")

    VideoFrame = Frame(self.main_frame, bg='gray20')
    VideoFrame.pack()

    BtnsFrame = Frame(self.main_frame, bg='gray20')
    BtnsFrame.pack()

    Button(BtnsFrame, text='Play', width=10, command=self.play).grid(row=0, column=0, padx=10, pady=10)
    Button(BtnsFrame, text='Pause', width=10, command=self.pause).grid(row=0, column=1)
    Button(BtnsFrame, text='Stop', width=10, command=self.stop).grid(row=0, column=2, padx=10, pady=10)

    self.videoplayer = vp.TkinterVideo(VideoFrame, scaled=True)
    self.videoplayer.load(self.video)
    self.videoplayer.pack(ipadx=160, ipady=80, pady=10)
