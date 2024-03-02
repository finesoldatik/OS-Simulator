from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfile, askopenfile

from res.modules.app import app


class App(app):
  def __init__(self, win, args=None):
    super().__init__(win=win, main_func="main", name="Блокнот")
    self.set_size(30, 17.5)
    self.filename = NONE

  def new_file(self):
    self.filename = "Untitled"
    self.text.delete('1.0', END)

  def save_file(self):
    data = self.text.get('1.0', END)
    with open(f"Storage/Documents/{self.filename}.txt", 'w') as f:
      f.write(data)

  def save_as(self):
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = self.text.get('1.0', END)
    try: out.write(data.rstrip())
    except Exception: showerror(title="Error", message="Saving file error")

  def open_file(self):
    inp = askopenfile(mode="r")
    if inp is None:
      return
    self.filename = inp.name
    data = inp.read()
    self.text.delete('1.0', END)
    self.text.insert('1.0', data)

  def main(self):
    self.text = Text(self.main_frame, width=50, height=30, wrap="word")
    scrollb = Scrollbar(self.main_frame, orient=VERTICAL, command=self.text.yview)
    scrollb.pack(side="right", fill="y")
    self.text.configure(yscrollcommand=scrollb.set)

    self.text.pack()
    fileMenu = Menu(self.menu, tearoff=0)
    fileMenu.add_command(label="Новый", command=self.new_file)
    fileMenu.add_command(label="Открыть", command=self.open_file)
    fileMenu.add_command(label="Сохранить", command=self.save_file)
    fileMenu.add_command(label="Сохранить как", command=self.save_as)
    self.menu.add_cascade(label="Файл", menu=fileMenu)
