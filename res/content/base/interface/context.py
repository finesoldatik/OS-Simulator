from tkinter import *

class Context:
  def __init__(self, win):
    self.win = win

    self.context = Menu(self.win, tearoff=0)
    self.create = Menu(self.context, tearoff=0)
    self.base_programs = Menu(self.context, tearoff=0)
    self.taskmenu = Menu(self.context, tearoff=0)
    self.base_programs.add_command(label="Музыка", command=lambda: self.win.program_handler.start("base.music"))
    self.base_programs.add_command(label="Видео", command=lambda: self.win.program_handler.start("base.video"))
    self.base_programs.add_command(label="Холст", command=lambda: self.win.program_handler.start("base.paint"))
    self.base_programs.add_command(label="Блокнот", command=lambda: self.win.program_handler.start("base.notepad"))
    self.base_programs.add_command(label="Проводник", command=lambda: self.win.program_handler.start("base.explorer"))
    self.base_programs.add_command(label="Калькулятор", command=lambda: self.win.program_handler.start("base.calculator"))
    self.base_programs.add_command(label="Терминал", command=lambda: self.win.program_handler.start("base.terminal"))

    self.taskmenu.add_command(label="Скрыть", command=self.win.desktop.hide_taskbar)
    self.taskmenu.add_command(label="Показать", command=self.win.desktop.show_taskbar)

    self.context.add_cascade(label="Открыть", menu=self.base_programs)
    self.context.add_cascade(label="Панель задач", menu=self.taskmenu)
    self.context.add_separator()
    self.context.add_command(label="Выйти", command=quit)

  def do_popup(self, event):
    try: self.context.tk_popup(event.x_root, event.y_root)
    finally: self.context.grab_release()
