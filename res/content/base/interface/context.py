from tkinter import *

class Context:
  def __init__(self, win):
    self.win = win

    self.context = Menu(self.win, tearoff=0)
    self.create = Menu(self.context, tearoff=0)
    self.base_programs = Menu(self.context, tearoff=0)
    self.taskmenu = Menu(self.context, tearoff=0)
    self.base_programs.add_command(label="Музыка", command=lambda: self.win.program_handler.start(program_import_path="base.music", position=[self.x, self.y]))
    self.base_programs.add_command(label="Видео", command=lambda: self.win.program_handler.start(program_import_path="base.video", position=[self.x, self.y]))
    self.base_programs.add_command(label="Холст", command=lambda: self.win.program_handler.start(program_import_path="base.paint", position=[self.x, self.y]))
    self.base_programs.add_command(label="Блокнот", command=lambda: self.win.program_handler.start(program_import_path="base.notepad", position=[self.x, self.y]))
    self.base_programs.add_command(label="Проводник", command=lambda: self.win.program_handler.start(program_import_path="base.explorer", position=[self.x, self.y]))
    self.base_programs.add_command(label="Калькулятор", command=lambda: self.win.program_handler.start(program_import_path="base.calculator", position=[self.x, self.y]))
    self.base_programs.add_command(label="Терминал", command=lambda: self.win.program_handler.start(program_import_path="base.terminal", position=[self.x, self.y]))
    self.base_programs.add_command(label="Редактор", command=lambda: self.win.program_handler.start(program_import_path="base.editor.main", position=[self.x, self.y]))
    self.create.add_command(label="Ярлык", command=lambda: self.win.program_handler.start(program_import_path="base.create.tag", position=[self.x, self.y]))

    self.taskmenu.add_command(label="Скрыть", command=self.win.desktop.hide_taskbar)
    self.taskmenu.add_command(label="Показать", command=self.win.desktop.show_taskbar)

    self.context.add_cascade(label="Открыть", menu=self.base_programs)
    self.context.add_cascade(label="Создать", menu=self.create)
    self.context.add_cascade(label="Панель задач", menu=self.taskmenu)
    self.context.add_separator()
    self.context.add_command(label="Выйти", command=quit)

  def do_popup(self, event):
    try:
      self.context.tk_popup(event.x_root, event.y_root)
      self.x = event.x_root
      self.y = event.y_root
    finally: self.context.grab_release()
