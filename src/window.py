from tkinter import *
from typing import List

from res.api.handlers import ProcessHandler, ProgramHandler

class Window(Tk):
  """Класс Window используется для создания окна симулятора ОС

    Основное применение - создание окна для работы с различными интерфейсами
    
    Attributes
    ----------
    context : type
        контекстное меню интерфейса, передается при стандартном запуске
    desktop : type
        рабочий стол интерфейса, передается при стандартном запуске

    Methods
    -------
    rgb(rgb: List[int]) -> str
        переводит RGB формат в HEX и возвращает строку
  """
  def __init__(self, context: type, desktop: type, system_path: str):
    super().__init__()
    self.title("OS Simulator")
    self.config(bg="gray10")
    self.wm_attributes("-fullscreen", True)
    self.screenwidth = self.winfo_screenwidth()
    self.screenheight = self.winfo_screenheight()
    self.opened_programs = []
    self.system_path:str = system_path
    self.default_program_movement_type:bool = True

    # Шрифты
    self.font = ('Consolas', 10, 'bold')

    # Запуск стартовых процессов
    ProcessHandler.run_startup(self)

    self.desktop = desktop(self)
    self.context = context(self)
    self.desktop.add_context()
    self.programslist = self.desktop.programslist
    self.program_handler = ProgramHandler(win=self, opened_programs=self.opened_programs, programslist=self.programslist)

  def rgb(self, rgb: List[int]) -> str:
    """Переводит из RGB формата в HEX и возвращает строку.

      Parameters
      ----------
      rgb : List[int]
          цвет в формате RGB (0, 0, 0)
    """
    return "#%02x%02x%02x" % rgb