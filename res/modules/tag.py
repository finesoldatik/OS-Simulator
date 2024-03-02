from tkinter import *
class Tag:
  def __init__(self, win, name, value, args):
    self.win = win
    self.name = name
    self.value = value
    self.args = args

  def create(self):
    name = ""
    if len(self.name) > 16:
      for i in self.name:
        if len(name) < 13: name += i
        else:
          name += "..."
          break
    else: name = self.name
    self.label = Button(master=self.win, text=name, font=self.win.font, width=16, command=lambda: self.win.program_handler.start(self.value, self.args))
