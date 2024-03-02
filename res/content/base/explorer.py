from tkinter import *
from ctypes import windll
from os import mkdir, listdir, path, startfile
from pathlib import Path

from res.modules.app import app


class App(app):
  def __init__(self, win, args=None):
    super().__init__(win=win, main_func="main", title="Проводник")
    self.set_size(30, 19.8)

  def main(self):
    windll.shcore.SetProcessDpiAwareness(True)

    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)

    self.new_file_name = StringVar(self.main_frame, "document.txt", 'new_name')
    self.current_path = StringVar(self.main_frame, name='current_path', value=Path.cwd())

    self.current_path.trace('w', self.path_change)

    Button(self.main_frame, text='Назад', command=self.go_back).grid(sticky=NSEW, column=0, row=0)

    self.main_frame.bind("<Alt-Left>", self.go_back)

    Button(self.main_frame, text='Создать', command=self.window_new_file_or_folder).grid(sticky=NSEW, column=0, row=1)

    Entry(self.main_frame, textvariable=self.current_path).grid(sticky=NSEW, column=1, row=0, ipady=10, ipadx=10)

    self.list = Listbox(self.main_frame, width=80, height=16)
    self.list.grid(sticky=NSEW, column=1, row=1, ipady=10, ipadx=10)

    self.list.bind('<Double-1>', self.change_path_by_click)
    self.list.bind('<Return>', self.change_path_by_click)

    self.path_change('')

  def path_change(self, *event):
    directory = listdir(self.current_path.get())
    self.list.delete(0, END)

    for file in directory:
        self.list.insert(0, file)

  def change_path_by_click(self, event=None):
    picked = self.list.get(self.list.curselection()[0])
    path_ = path.join(self.current_path.get(), picked)

    if path.isfile(path_): startfile(path_)
    else: self.current_path.set(path_)

  def go_back(self, event=None):
    new_path = Path(self.current_path.get()).parent
    self.current_path.set(new_path)

  def window_new_file_or_folder(self):
    self.new_window = Frame(self.main_frame)
    self.new_window.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(self.new_window, text='Введите название нового файла/папки').grid()
    Entry(self.new_window, textvariable=self.new_file_name).grid(column=0, pady=10, sticky=NSEW)
    Button(self.new_window, text="Создать", command=self.new_file_or_folder).grid(pady=10, sticky=NSEW)
    Button(self.new_window, text="Закрыть", command=lambda: self.new_window.destroy()).grid(pady=10, sticky=NSEW)

  def new_file_or_folder(self):
    if len(self.new_file_name.get().split('.')) != 1: open(path.join(self.current_path.get(), self.new_file_name.get()), 'w').close()
    else: mkdir(path.join(self.current_path.get(), self.new_file_name.get()))

    self.new_window.destroy()
    self.path_change()