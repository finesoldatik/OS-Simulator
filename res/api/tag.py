"""
Модуль tag помогает создавать ярлыки рабочего стола симулятора ОС.

finesoldatik
finesoldat@gmail.com
# License: MIT
"""
__author__ = 'finesoldatik'

__version__ = "0.0.1"

from tkinter import *

class Tag:
  """Класс Tag используется для создания ярлыков приложений на рабочем столе

    Основное применение - создание ярлыков на рабочем столе

    Attributes
    ----------
    win : Window
        окно симулятора ОС
    name: str
        имя ярлыка
    value: str
        значение ярлыка
            (ссылка на приложение)
    args: list
        аргументы ярлыка
            (передаются приложению)

    Methods
    -------
    create()
        создает ярлык приложения
  """
  def __init__(self, win, name: str, value: str, args: dict):
    self.win = win
    self.name: str = name
    self.value: str = value
    self.args: dict = args

  def create(self):
    """Создает ярлык приложения.
    """
    name = ""
    if len(self.name) > 16:
      for i in self.name:
        if len(name) < 13:
          name += i
        else:
          name += "..."
          break
    else:
      name = self.name
    self.label = Button(master=self.win, text=name, font=self.win.font, width=16, command=lambda: self.win.program_handler.start(self.value, self.args))
