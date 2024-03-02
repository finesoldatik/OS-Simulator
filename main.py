from tkinter import *
from os import path, mkdir
from importlib import import_module

from res.modules.process_handler import ProcessHandler
from res.modules.program_handler import ProgramHandler

class Window(Tk):
  def __init__(self, context, desktop):
    super().__init__()
    self.title("OS Simulator")
    self.config(bg="gray10")
    self.wm_attributes("-fullscreen", True)
    self.screenwidth = self.winfo_screenwidth()
    self.screenheight = self.winfo_screenheight()
    self.opened_programs = []
    self.system_path = f"{path.dirname(__file__)}\\"

    # цвета
    self.normal = self.rgb((234, 234, 234))

    # шрифты
    self.font = ('Consolas', 10, 'bold')

    # запуск необходимых процессов для запуска
    ProcessHandler.run_startup(self)

    self.desktop = desktop(self)
    self.programs = self.desktop.programs
    self.program_handler = ProgramHandler(win=self, opened_programs=self.opened_programs, programs=self.programs)
    self.context = context(self)
    self.desktop.add_context()

  def rgb(self, rgb): return "#%02x%02x%02x" % rgb

  def create_folder(self, path_=""): mkdir(f"storage\\{path_}\\Новая папка")

  def create_document(self):
    with open("storage\\{path_}\\Новый документ.txt") as f: f.close()

  def create_image(self):
    with open("storage\\{path_}\\Новое изображение.png") as f: f.close()

if __name__ == "__main__":
  name = "base"
  context = import_module(f"res.modules.{name}.context")
  desktop = import_module(f"res.modules.{name}.desktop")
  win = Window(context=context.Context, desktop=desktop.Desktop)
  win.mainloop()