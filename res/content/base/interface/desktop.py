from tkinter import *

from res.modules.desktop import desktop

class Desktop(desktop):
  def __init__(self, win):
    super().__init__(win=win)

    self.add_wallpaper("\\storage\\Images\\Wallpapers\\wallpaper.jpg")

    self.add_tags()

    self.add_taskbar()
