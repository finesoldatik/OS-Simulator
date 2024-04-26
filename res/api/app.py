"""
Модуль app облегчает создание приложения для симулятора ОС.

finesoldatik
finesoldat@gmail.com
# License: MIT
"""
__author__ = 'finesoldatik'

__version__ = "0.0.1"

from tkinter import *

class app(Frame):
  """Класс app облегчает создание приложения для симулятора ОС

    Основное применение - создание приложения для симулятора ОС

    Attributes
    ----------
    win : Window
        окно симулятора ОС
    position : list=[tkinter.CENTER, tkinter.CENTER]
        координаты запуска приложения
    main_func : str="main"
        главная функция приложения
            (с нее начинает работать приложение)
    title : str="Программа"
        заголовок приложения

    Methods
    -------
    exit()
        завершает работу приложения
    center()
        центрирует приложение относительно рабочего стола
    hide()
        прячет приложение
    show()
        показывает приложение
    start(main_func:str="main", title:str = "Программа")
        запускает приложение
            (выполняется по умолчанию)
    add_menu()
        добавляет меню приложения
            (выполняется по умолчанию)
    start_move_app(event: tkinter.Event)
        начинает перемещение окна приложения
            (выполняется автоматически)
    final_move_app(event: tkinter.Event)
        оканчивает перемещение окна приложения
            (выполняется автоматически)
    move_app(event: tkinter.Event)
        перемещает окно приложения
            (выполняется автоматически)
  """
  def __init__(self, win, position: list=[CENTER, CENTER], main_func: str="content", title: str="Приложение"):
    super().__init__(win)
    self.win = win
    self.position: list = position
    self.hiden: bool = False
    self.x: int = 0
    self.y: int = 0
    self.start(main_func, title)

  def exit(self):
    """Завершает работу приложения.
    """
    self.win.programslist.delete(self.win.opened_programs.index(self))
    self.win.opened_programs.remove(self)
    self.destroy()

  def center(self):
    """Центрирует приложение относительно рабочего стола.
    """
    self.place_forget()
    self.place(relx=0.5, rely=0.5, anchor=CENTER)
  
  def hide(self):
    """Прячет приложение.
    """
    self.place_forget()
    self.hiden = True
  
  def show(self):
    """Показывает приложение.
    """
    self.place(relx=0.5, rely=0.5, anchor=CENTER)
    self.hiden = False

  def start(self, main_func: str="main", title: str="Программа"):
    """Запускает приложение.
          (выполняется по умолчанию)

      Parameters
      ----------
      main_func : str="main"
          главная функция приложения
              (с нее начинает работать приложение)
      title : str="Программа"
          заголовок приложения
    """
    if self.position == [CENTER, CENTER]:
      self.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
      self.place(x=self.position[0], y=self.position[1])

    self.top = Frame(self)
    self.top.pack(fill=X)

    self.title = Label(self.top, text=title)
    self.title.pack(side=LEFT, expand=True)

    self.quitBtn = Button(self.top, text='X', bg='red', fg='white', font=self.win.font, border=0, width=3, command=self.exit)
    self.quitBtn.pack(side=RIGHT)

    self.hideBtn = Button(self.top, text='-', bg='gray30', fg='white', font=self.win.font, border=0, width=3, command=self.hide)
    self.hideBtn.pack(side=RIGHT)

    self.main_frame = Frame(self)
    self.main_frame.pack()

    self.top.bind('<ButtonPress-1>', self.start_move_app)
    self.title.bind('<ButtonPress-1>', self.start_move_app)
    self.top.bind('<ButtonRelease-1>', self.final_move_app)
    self.title.bind('<ButtonRelease-1>', self.final_move_app)
    self.top.bind('<B1-Motion>', self.move_app)
    self.title.bind('<B1-Motion>', self.move_app)

    self.menu = Menu(self.main_frame, tearoff=0)
    self.win.config(menu=self.menu)

    self.win.update_idletasks()
    getattr(self, main_func)()
    self.add_menu()

  def add_menu(self):
    """Добавляет меню приложения.
          (выполняется по умолчанию)
    """
    self.app_menu = Menu(self.menu, tearoff=0)

    self.placement_menu = Menu(self.app_menu, tearoff=0)
    self.placement_menu.add_command(label="Центр", command=self.center)
    self.app_menu.add_cascade(label="Расположение", menu=self.placement_menu)

    self.app_menu.add_command(label="Скрыть", command=self.hide)
    self.app_menu.add_command(label="Показать", command=self.show)
    self.app_menu.add_command(label="Закрыть", command=self.exit)

    self.menu.add_cascade(label="Приложение", menu=self.app_menu)
  
  def start_move_app(self, event: Event):
    """Начинает передвижение окна.
          (выполняется автоматически)

      Parameters
      ----------
      event : tkinter.Event
        tkinter.Event
    """
    width = self.winfo_width()
    height = self.winfo_height()
    self.place_forget()
    self.win.config(menu=self.menu)
    
    if self.win.default_program_movement_type:
      self.place(x=event.x_root, y=event.y_root)
    else:
      self.moveFrame = Frame(self.win, bg="#4287f5", width=width, height=height)
      Frame(self.moveFrame, bg="#0e55c7", width=width, height=height).pack(padx=5, pady=5)
      self.moveFrame.place(x=event.x_root, y=event.y_root)
  
  def final_move_app(self, event: Event):
    """Оканчивает передвижение окна.
          (выполняется автоматически)

      Parameters
      ----------
      event : tkinter.Event
        tkinter.Event
    """
    try:
      self.place(x=self.x, y=self.y)
    except:
      self.place(x=event.x_root, y=event.y_root)
    if not self.win.default_program_movement_type:
      self.moveFrame.destroy()

  def move_app(self, event: Event):
    """Перемещает окно приложения.
          (выполняется автоматически)

      Parameters
      ----------
      event : tkinter.Event
        tkinter.Event
    """

    self.x = event.x_root - self.win.desktop.wall.winfo_rootx()
    self.y = event.y_root - self.win.desktop.wall.winfo_rooty()

    if self.win.default_program_movement_type:
      self.place(x=self.x, y=self.y)
    else:
      self.moveFrame.place(x=self.x, y=self.y)
