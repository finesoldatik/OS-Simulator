from tkinter import *

from res.modules.handlers import ProcessHandler, ProgramHandler

class Window(Tk):
  """Создает окно симулятора."""
  def __init__(self, context, desktop, system_path):
    super().__init__()
    self.title("OS Simulator")
    self.config(bg="gray10")
    self.wm_attributes("-fullscreen", True)
    self.screenwidth = self.winfo_screenwidth()
    self.screenheight = self.winfo_screenheight()
    self.opened_programs = []
    self.system_path = system_path

    # цвета
    self.normal = self.rgb((234, 234, 234))

    # шрифты
    self.font = ('Consolas', 10, 'bold')

    # запуск необходимых процессов для запуска
    ProcessHandler.run_startup(self)

    self.desktop = desktop(self)
    self.context = context(self)
    self.desktop.add_context()
    self.programslist = self.desktop.programslist
    self.program_handler = ProgramHandler(win=self, opened_programs=self.opened_programs, programslist=self.programslist)

  def rgb(self, rgb):
    """Перевод RGB формата в HEX для работы с tkinter."""
    return "#%02x%02x%02x" % rgb