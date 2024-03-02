from tkinter import *
import tkVideoPlayer as vp

from res.modules.app import app


class App(app):
  def __init__(self, win, args=None):
    super().__init__(win=win, main_func="main", title="Видео")
    self.set_size(30.1, 23)
    self.args = args
    self.config(bg="gray20")
    
  def play(self):
    self.video.play()

  def pause(self):
    self.video.pause()

  def stop(self):
    self.video.stop()

  def main(self):
    VideoFrame = Frame(self, bg='gray20')
    VideoFrame.pack()

    BtnsFrame = Frame(self, bg='gray20')
    BtnsFrame.pack()

    Button(BtnsFrame, text='Play', width=10, command=self.play).grid(row=0, column=0, padx=10, pady=10)
    Button(BtnsFrame, text='Pause', width=10, command=self.pause).grid(row=0, column=1)
    Button(BtnsFrame, text='Stop', width=10, command=self.stop).grid(row=0, column=2, padx=10, pady=10)

    self.video = vp.TkinterVideo(VideoFrame, scaled=True)
    self.video.load(self.event)
    self.video.pack(ipadx=160, ipady=80, pady=10)
