from tkinter import *

class app(Frame):
  def __init__(self, win, position, main_func:str = "main", title:str = "Программа"):
    super().__init__(win)
    self.win = win
    self.position:list = position
    self.hiden = False
    self.x = 0
    self.y = 0
    self.start(main_func, title)

  def exit(self):
    """Закрывает приложение."""
    self.win.programslist.delete(self.win.opened_programs.index(self))
    self.win.opened_programs.remove(self)
    self.destroy()

  def center(self):
    """Центрирует приложение."""
    self.place_forget()
    self.place(relx=0.5, rely=0.5, anchor=CENTER)
  
  def hide(self):
    self.place_forget()
    self.hiden = True
  
  def show(self):
    self.place(relx=0.5, rely=0.5, anchor=CENTER)
    self.hiden = False

  def start(self, main_func:str, title:str = "Программа"):
    """Выводит приложение на экран. Необходима главная функция с базовым интерфейсом программы и её заголовок."""
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
    """Добавляет меню приложения"""
    self.placement = Menu(self.menu, tearoff=0)
    self.placement.add_command(label="Центр", command=self.center)

    self.menu.add_cascade(label="Расположение", menu=self.placement)

    self.menu.add_command(label="Закрыть", command=self.exit)
  
  def start_move_app(self, e):
    """Прячет окно программы и создает окно для перемещения, устанавливает меню приложения"""
    width = self.winfo_width()
    height = self.winfo_height()
    self.place_forget()
    self.win.config(menu=self.menu)
    
    if self.win.default_program_movement_type:
      self.place(x=e.x_root, y=e.y_root)
    else:
      self.moveFrame = Frame(self.win, bg="#4287f5", width=width, height=height)
      Frame(self.moveFrame, bg="#0e55c7", width=width, height=height).pack(padx=5, pady=5)
      self.moveFrame.place(x=e.x_root, y=e.y_root)
  
  def final_move_app(self, e):
    """Устанавливает окно программы в конечную точку и удаляет временное окно для перемещения."""
    try:
      self.place(x=self.x, y=self.y)
    except:
      self.place(x=e.x_root, y=e.y_root)
    if not self.win.default_program_movement_type:
      self.moveFrame.destroy()

  def move_app(self, e):
    """Передвигает временное окно для перемещения."""

    self.x = e.x_root - self.win.desktop.wall.winfo_rootx()
    self.y = e.y_root - self.win.desktop.wall.winfo_rooty()

    if self.win.default_program_movement_type:
      self.place(x=self.x, y=self.y)
    else:
      self.moveFrame.place(x=self.x, y=self.y)
