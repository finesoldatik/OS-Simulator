from time import localtime, strftime
from tkinter import *
from PIL import Image, ImageTk

from res.modules.tag import Tag
from res.modules.handlers import JsonHandler

class Desktop:
  def __init__(self, win):
    self.win = win
    self.tags = JsonHandler.read("res\\tags.json")
    self.tags_max = 7

    wallpaper = self.wallpaper("\\storage\\Images\\Wallpapers\\wallpaper.jpg")
    self.wall = Label(self.win, image=wallpaper)
    self.wall.image = wallpaper
    self.wall.place(x=-2, y=-2)

    # tags
    x = 90
    y = 10
    tags_count = 0
    for name in self.tags:
      if tags_count / self.tags_max == 1:
        x = 90
        y += 50
      tags_count += 1
      tag = Tag(win=self.win, name=name, value=self.tags.get(name)[0], args=self.tags.get(name)[1])
      tag.create()
      tag.label.place(x=x, y=y)
      x += 130

    # taskbar
    self.taskbar = Frame(self.win, background="gray20")
    self.taskbar.place(x=0, y=0)

    self.system_time = Label(self.taskbar, text='', bg='gray20', fg='white', font=self.win.font)
    self.system_time.grid(column=0, row=0)

    self.programs = Listbox(self.taskbar, width=12, height=30, borderwidth=0, bg="gray25", fg="white", selectbackground="gray25", highlightbackground="gray25")
    self.programs.grid(column=0, row=1, pady=1)

    self.programs.bind("<Button-1>", self.get_prog)

    self.time_update()

  def add_context(self):
    self.wall.bind("<Button-3>", self.win.context.do_popup)

  def wallpaper(self, bg):
    wallpaper = Image.open(self.win.system_path + bg)
    wallpaper = wallpaper.resize((self.win.screenwidth, self.win.screenheight), Image.LANCZOS)
    wallpaper = ImageTk.PhotoImage(wallpaper)

    return wallpaper

  def get_prog(self, e):
    selection = e.widget.curselection()
    if len(selection) > 0:
      index = selection[0]
      self.win.config(menu=self.win.opened_programs[index].menu)

  def hide_taskbar(self): self.taskbar.place_forget()
  def view_taskbar(self): self.taskbar.place(x=0, y=0)

  def time_update(self):
    local = localtime()
    time_str = strftime("%H:%M:%S\n%d/%m/%Y", local)
    self.system_time.configure(text=time_str)
    self.win.after(1000, self.time_update)
