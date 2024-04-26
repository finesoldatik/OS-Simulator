from tkinter import *

from res.api.app import app
from res.api.handlers import ProcessHandler

class App(app):
  def __init__(self, win, position, args={}):
    self.output = ""
    super().__init__(win=win, position=position, title="Терминал")
  
  def content(self):
    self.output_label = Label(self.main_frame)
    self.output_label.pack()
    self.entry = Entry(self.main_frame)
    self.entry.pack()
    self.entry.bind("<Return>", self.cmd)

  def cmd(self, e):
    cmd = self.entry.get()
    cmd = cmd.lower()
    if cmd not in ["", " ", "  ", "   "]:
      cmd = cmd.split()
    if len(cmd) > 1:
      if cmd[0] == "sapp":
        self.output = self.win.program_handler.start(program_import_path=cmd[1])
        print(cmd[1:])
      if cmd[0] == "sproc":
        self.output = ProcessHandler.start(cmd[1])
      if self.output != "":
        self.output_label.config(text=self.output)
    else:
      if cmd[0] == "oprogs":
        programs = ""
        for program in self.win.opened_programs:
          programs += f"{program.name['text']}\n"
        self.output = programs
      if self.output != "":
        self.output_label.config(text=self.output)
