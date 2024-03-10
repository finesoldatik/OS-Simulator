from tkinter import *

from importlib import import_module

from res.api.app import app
from res.api.handlers import JSONHandler

class App(app):
  def __init__(self, win, position, args={}):
    super().__init__(win=win, position=position, title="Создать ярлык")

  def add(self):
    name = self.name.get()
    path = self.path.get()

    try:
      import_module(f"res.content.{path}")
      self.result.config(text="Успешно!", fg="green")
      exists = True
    except:
      self.result.config(text="Приложение не найдено!", fg="red")
      exists = False

    if name not in ['', '  ', '   ', '    ', '     '] and path not in ['', '  ', '   ', '    ', '     '] and exists:

      data = JSONHandler.read('res\\tags.json')

      data[name] = [path, {}]

      JSONHandler.write('res\\tags.json', data)

      self.name.delete(0, END)
      self.path.delete(0, END)

  def main(self):
    Label(self.main_frame, text="Введите имя ярлыка").pack()

    self.name = Entry(self.main_frame)
    self.name.pack()

    Label(self.main_frame, text="Введите путь импорта вашего приложения\nотносительно res.content.").pack()

    self.path = Entry(self.main_frame)
    self.path.pack()

    Button(self.main_frame, text="Добавить", command=self.add).pack()

    self.result = Label(self.main_frame, text="", fg="red")
    self.result.pack()
