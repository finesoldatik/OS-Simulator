from tkinter import *

from res.modules.app import app
from res.modules.handlers import ProcessHandler


class App(app):
  def __init__(self, win, args=None):
    super().__init__(win=win, main_func="main", title="Терминал")
    self.set_size(30.1, 23)
    self.output = ""

  def cmd(self, e):
    cmd = self.entry.get()
    cmd = cmd.lower()
    if cmd not in ["", " ", "  ", "   "]:
      cmd = cmd.split()
    if len(cmd) > 1:
      if cmd[0] == "sapp": self.output = self.win.program_handler.start(cmd[1])
      if cmd[0] == "sproc": self.output = ProcessHandler.start(cmd[1])
      if self.output != "": self.output_label.config(text=self.output)
    else:
      if cmd[0] == "oprogs":
        programs = ""
        for program in self.win.opened_programs:
          programs += f"{program.name['text']}\n"
        self.output = programs
      if self.output != "": self.output_label.config(text=self.output)

  def main(self):
    self.output_label = Label(self.main_frame)
    self.output_label.pack()
    self.entry = Entry(self.main_frame)
    self.entry.pack()
    self.entry.bind("<Return>", self.cmd)
