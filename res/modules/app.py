from tkinter import *

class app(Frame):
  def __init__(self, win, main_func:str = "main", title:str = "Программа"):
    super().__init__(win)
    self.win = win
    self.start(main_func, title)

  def exit(self):
    """Закрывает приложение."""
    self.win.programs.delete(self.win.opened_programs.index(self))
    self.win.opened_programs.remove(self)
    self.destroy()

  def center(self):
    """Центрирует приложение."""
    self.place_forget()
    self.place(relx=0.5, rely=0.5, anchor=CENTER)

  def start(self, main_func:str, title:str = "Программа"):
    """Выводит приложение на экран. Необходима главная функция с базовым интерфейсом программы и её заголовок."""
    self.place(relx=0.5, rely=0.5, anchor=CENTER)

    self.top = Frame(self)
    self.top.pack(fill=X)

    self.title = Label(self.top, text=title)
    self.title.pack(side=LEFT, expand=True)

    self.quitBtn = Button(self.top, text='X', bg='red', fg='white', font=self.win.font, border=0, width=3, command=self.exit)
    self.quitBtn.pack(side=RIGHT)

    self.main_frame = Frame(self)
    self.main_frame.pack()

    self.top.bind('<B1-Motion>', self.move_app)
    self.title.bind('<B1-Motion>', self.move_app)

    self.menu = Menu(self.main_frame, tearoff=0)
    self.win.config(menu=self.menu)

    self.win.update_idletasks()
    getattr(self, main_func)()
    self.add_menu()

  def add_menu(self):
    """Добавляет меню приложения"""
    self.placement = Menu(self.menu, tearoff=0)
    self.placement.add_command(label="Центр", command=self.center)

    self.menu.add_cascade(label="Расположение", menu=self.placement)
    self.menu.add_command(label="Закрыть", command=self.exit)

  def set_size(self, width:float, height:float):
    """Корректирующие парамметры, обязательны для настройки передвижения окна."""
    self.width = width
    self.height = height

  def move_app(self, e):
    """Передвигает окно."""
    self.place(x=e.x_root - self.width * self.width, y=e.y_root - self.height * self.height)
    self.win.config(menu=self.menu)
