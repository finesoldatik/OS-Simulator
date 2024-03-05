from tkinter import *
from PIL import Image, ImageTk
from time import localtime, strftime

from res.modules.handlers import JsonHandler
from res.modules.tag import Tag

class desktop:
  def __init__(self, win):
    self.win = win
    self.tags = JsonHandler.read("res\\tags.json")
  
  def add_wallpaper(self, wallpaper_path:str):
    """Добавляет фоновую картинку (обои)"""
    wallpaper = self.change_wallpaper(wallpaper_path)
    self.wall = Label(self.win, image=wallpaper)
    self.wall.image = wallpaper
    self.wall.place(x=-2, y=-2)
  
  def change_wallpaper(self, wallpaper_path:str):
    """Изменяет фоновую картинку (обои). Необходимо, чтобы они были добавлены с помощью self.add_wallpaper() до запуска этой функции"""
    wallpaper = Image.open(self.win.system_path + wallpaper_path)
    wallpaper = wallpaper.resize((self.win.screenwidth, self.win.screenheight), Image.LANCZOS)
    wallpaper = ImageTk.PhotoImage(wallpaper)

    return wallpaper
  
  def add_tags(self, x:int=90, y:int=10, tags_max:int=7):
    """Добавляет ярлыки, загруженные из tags.json"""
    tags_count = 0
    for name in self.tags:
      if tags_count / tags_max == 1:
        x = 90
        y += 50
      tags_count += 1
      tag = Tag(win=self.win, name=name, value=self.tags.get(name)[0], args=self.tags.get(name)[1])
      tag.create()
      tag.label.place(x=x, y=y)
      x += 130
  
  def add_context(self):
    """Добавляет контекстное меню (Автоматически в window.py, не рекомендуется использовать, может привести к ошибкам)."""
    self.wall.bind("<Button-3>", self.win.context.do_popup)

  def add_taskbar(self):
    """Добавляет таскбар по умолчанию"""
    self.taskbar = Frame(self.win, background="gray20")
    self.taskbar.place(x=0, y=0)

    self.system_time = Label(self.taskbar, text='', bg='gray20', fg='white', font=self.win.font)
    self.system_time.grid(column=0, row=0)

    self.programslist = Listbox(self.taskbar, width=12, height=30, borderwidth=0, bg="gray25", fg="white", selectbackground="gray25", highlightbackground="gray25")
    self.programslist.grid(column=0, row=1, pady=1)

    self.programslist.bind("<Button-1>", self.get_prog)

    self.time_update()

  def get_prog(self, e):
    """Запускает программу выбранную в списке запущенных программ"""
    selection = e.widget.curselection()
    if len(selection) > 0:
      index = selection[0]
      program = self.win.opened_programs[index]
      self.win.config(menu=program.menu)
      if program.hiden:
        program.show()

  def hide_taskbar(self):
    """Прячет таскбар по умолчанию"""
    self.taskbar.place_forget()

  def show_taskbar(self):
    """Показывает таскбар по умолчанию"""
    self.taskbar.place(x=0, y=0)

  def time_update(self):
    local = localtime()
    time_str = strftime("%H:%M:%S\n%d/%m/%Y", local)
    self.system_time.configure(text=time_str)
    self.win.after(1000, self.time_update)