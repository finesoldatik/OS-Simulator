"""
Модуль desktop предлагает несколько базовых функций
    рабочего стола симулятора ОС.

finesoldatik
finesoldat@gmail.com
# License: MIT
"""
__author__ = 'finesoldatik'

__version__ = "0.0.1"

from tkinter import *
from PIL import Image, ImageTk
from time import localtime, strftime

from res.api.handlers import JSONHandler
from res.api.tag import Tag

class desktop:
  """Класс desktop используется для создания базового рабочего стола симулятора ОС

    Основное применение - создание базового рабочего стола для работы с вашей псевдо ОС

    Attributes
    ----------
    win : Window
        окно симулятора ОС

    Methods
    -------
    add_wallpaper(wallpaper_path: str)
        добавляет обои на ваш рабочий стол.
    change_wallpaper(wallpaper_path: str) -> PIL.ImageTk.PhotoImage
        возвращает обои, которые можно установить на рабочий стол
    add_tags(default_x: int=90, default_y: int=10, max_tags_in_line: int=7)
        добавляет ярлыки на рабочий стол
    add_context()
        разрешает контекстному меню появляться на рабочем столе
            при клике правой кнопкой мыши
    add_taskbar()
        добавляет панель задач на рабочий стол
    hide_taskbar()
        прячет панель задач
    show_taskbar()
        показывает панель задач
    get_prog(event)
        вызывает программу, выбранную на панели задач
    time_update()
        обновляет время на панели задач
  """
  def __init__(self, win):
    self.win = win
    self.tags: dict = JSONHandler.read("res\\tags.json")
  
  def add_wallpaper(self, wallpaper_path: str):
    """Добавляет фоновую картинку (обои) на ваш рабочий стол.

      Parameters
      ----------
      wallpaper_path : str
          путь до изображения (обоев)
    """
    wallpaper = self.change_wallpaper(wallpaper_path)
    self.wall = Label(self.win, image=wallpaper)
    self.wall.image = wallpaper
    self.wall.place(x=-2, y=-2)
  
  def change_wallpaper(self, wallpaper_path: str) -> ImageTk.PhotoImage:
    """Возвращает обои, которые можно установить на рабочий стол.

      Parameters
      ----------
      wallpaper_path : str
          путь до изображения (обоев)
    """
    wallpaper = Image.open(self.win.system_path + wallpaper_path)
    wallpaper = wallpaper.resize((self.win.screenwidth, self.win.screenheight), Image.LANCZOS)
    wallpaper = ImageTk.PhotoImage(wallpaper)

    return wallpaper
  
  def add_tags(self, default_x: int=90, default_y: int=10, max_tags_in_line: int=7):
    """Добавляет ярлыки на рабочий стол,
        загруженые из файла tags.json при запуске симулятора.

      Parameters
      ----------
      default_x : int=90
          X первого тега
              (остальные теги будут отталкиваться от этого X)
      default_y : int=10
          Y первого тега
              (остальные теги будут отталкиваться от этого Y)
      max_tags_in_line : int=7
          Количество тегов в 1 линии
              (их может быть несколько, исходя из числа тегов)
    """
    x: int = default_x
    y: int = default_y
    tags_count: int = 0
    for name in self.tags:
      if tags_count % max_tags_in_line == 0 and tags_count != 0:
        x = 90
        y += 50
      tags_count += 1
      tag = Tag(win=self.win, name=name, value=self.tags.get(name)[0], args=self.tags.get(name)[1])
      tag.create()
      tag.label.place(x=x, y=y)
      x += 130
  
  def add_context(self):
    """Разрешает контекстному меню появляться на рабочем столе
          при клике правой кнопкой мыши.
    """
    self.wall.bind("<Button-3>", self.win.context.do_popup)

  def add_taskbar(self):
    """Добавляет панель задач на рабочий стол.
    """
    self.taskbar = Frame(self.win, background="gray20")
    self.taskbar.place(x=0, y=0)

    self.system_time = Label(self.taskbar, text='', bg='gray20', fg='white', font=self.win.font)
    self.system_time.grid(column=0, row=0)

    self.programslist = Listbox(self.taskbar, width=12, height=30, borderwidth=0, bg="gray25", fg="white", selectbackground="gray25", highlightbackground="gray25")
    self.programslist.grid(column=0, row=1, pady=1)

    self.programslist.bind("<Button-1>", self.get_prog)

    self.time_update()

  def hide_taskbar(self):
    """Прячет панель задач.
    """
    self.taskbar.place_forget()

  def show_taskbar(self):
    """Показывает панель задач.
    """
    self.taskbar.place(x=0, y=0)

  def get_prog(self, event: Event):
    """Вызывает программу, выбранную на панели задач.

      Parameters
      ----------
      event : tkinter.Event
          tkinter.Event
    """
    selection = event.widget.curselection()
    if len(selection) > 0:
      index = selection[0]
      program = self.win.opened_programs[index]
      self.win.config(menu=program.menu)
      if program.hiden:
        program.show()

  def time_update(self):
    """Обновляет время на панели задач.
    """
    local = localtime()
    time_str = strftime("%H:%M:%S\n%d/%m/%Y", local)
    self.system_time.configure(text=time_str)
    self.win.after(1000, self.time_update)