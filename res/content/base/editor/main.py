from tkinter import *
from tkinter.messagebox import showerror
import ctypes
import re
import os
from pathlib import Path

from res.api.app import app

ctypes.windll.shcore.SetProcessDpiAwareness(True)

class btn:
  def __init__(self, master, enter="gray15", leave="gray20", touch="white", release="gray10", text="btn", fg="#eaeaea", bg="gray20", font_="Consolas 15", command=None):
    self.root = Button(master=master, text=text, bg=bg, fg=fg, font=font_, borderwidth=0, highlightthickness=0, command=command)
    self.root.bind('<Enter>', lambda e: self.paint(enter))
    self.root.bind('<Leave>', lambda e: self.paint(leave))
    self.root.bind('<Button-1>', lambda e: self.paint(touch))
    self.root.bind('<ButtonRelease-1>', lambda e: self.paint(release))

  def paint(self, color):
    self.root.config(bg=color, activebackground=color)

class App(app):
  def __init__(self, win, position, args={}):
    self.settings = {
      "normal": "#eaeaea",
      "number": "#4275f5",
      "bracket": "#ebf224",
      "class": "#19e37e",
      "constant": "#1948e3",
      "keywords": "#ea5f5f",
      "comments": "#5feaa5",
      "string": "#eaa25f",
      "function": "#5fd3ea",
      "background": "#2a2a2a",
      "font": "Consolas 15"
    }
    self.repl = [
      ['(^| |\(|\[|\{|\=|\>|\<)(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield|/|\*|\+|\-|\=|\>|\<)($| |\(|\[|\{|\=|\>|\<)', "#ea5f5f"], #keyword
      ['(^| |\(|\[|\{|\=|\>|\<)(print|eval|range|randint)($| |\(|\[|\{|\=|\>|\<)', "#5fd3ea"], #function
      ['(^| |\(|\[|\{|\=|\>|\<)(random|os|json)($| |\(|\[|\{|\=|\>|\<)', "#19e37e"], #class
      ['\d+', "#4275f5"], #num
      ['[(){}\[\]]', "#ebf224"], #bracket
      ['".*?"', "#eaa25f"], #string
      ['\'.*?\'', "#eaa25f"], #string
      ['#.*?$', "#5feaa5"], #comments
      ['[A-Z]{2}', "#1948e3"], #constant
    ]
    self.previousText = ''
    self.normal = self.settings.get('normal')
    self.keywords = self.settings.get('keywords')
    self.comments = self.settings.get('comments')
    self.string = self.settings.get('string')
    self.function = self.settings.get('function')
    self.background = self.settings.get('background')
    self.font = self.settings.get('font')
    self.tabs = 0

    self.current_path = StringVar(win, Path.cwd(), 'current_path')
    self.current_path.trace('w', self.path_change)

    super().__init__(win=win, position=position, title="Редактор")
  
  def path_change(self, *event):
    directory = os.listdir(self.current_path.get())
    self.files.delete(0, END)

    for file in directory:
      self.files.insert(0, file)

    self.files.insert(0, "../")

  def change_path_by_click(self, event=None):
    picked = self.files.get(self.files.curselection()[0])
    path = os.path.join(self.current_path.get(), picked)

    if os.path.isfile(path):
      try:
        with open(path, "r", encoding="utf-8") as f:
          read_data = f.read()
          f.close()

      except:
        read_data = "Файл не найден/невозможно прочитать!"

      self.editArea.delete("1.0", END)
      self.editArea.insert(END, read_data)
      self.changes()

    else:
      if picked == "../":
        self.go_back()
      else:
        self.current_path.set(path)

  def go_back(self, event=None):
    new_path = Path(self.current_path.get()).parent
    self.current_path.set(new_path)
  
  def create(self, type_):
    self.create_root = Frame(self.main_frame)
    self.create_root.place(relx=0.5, rely=0.5, anchor=CENTER)
    self.create_root.config(background="gray10")

    self.create_root.columnconfigure(0, weight=1)

    if type_ == 'file':
      Label(self.create_root, text='Введите название нового файла', font=self.font, fg=self.normal, bg="gray10").grid()
      self.filename = Entry(self.create_root, bg='gray20', insertbackground=self.normal, font=self.font, fg=self.normal)
      self.filename.grid(column=0, pady=3)
      submit = btn(self.create_root, text="Создать", command=self.new_file)
      submit.root.grid(pady=1)
    elif type_ == 'folder':
      Label(self.create_root, text='Введите название новой папки', font=self.font, fg=self.normal, bg="gray10").grid()
      self.filename = Entry(self.create_root, bg='gray20', insertbackground=self.normal, font=self.font, fg=self.normal)
      self.filename.grid(column=0, pady=3)
      submit = btn(self.create_root, text="Создать", command=self.new_folder)
      submit.root.grid(pady=1)
      
  def new_file(self):
    open(os.path.join(self.current_path.get(), self.filename.get()), 'w').close()
    self.create_root.destroy()
    self.path_change()
    
  def new_folder(self):
    os.mkdir(os.path.join(self.current_path.get(), self.filename.get()))
    self.create_root.destroy()
    self.path_change()
  
  def execute(self, event=None):
    with open(self.win.system_path + "res\\content\\base\\editor\\executed.py", 'w', encoding='utf-8') as f:
      f.write(self.editArea.get('1.0', END))
      f.close()

    os.system(f'start cmd /K python "{self.win.system_path}res\\content\\base\\editor\\executed.py"')

  def changes(self, event=None):
    if self.editArea.get('1.0', END) == self.previousText:
      return

    for tag in self.editArea.tag_names():
      self.editArea.tag_remove(tag, "1.0", "end")

    i = 0
    for pattern, color in self.repl:
      for start, end in self.search_re(pattern, self.editArea.get('1.0', END)):
        self.editArea.tag_add(f'{i}', start, end)
        self.editArea.tag_config(f'{i}', foreground=color)

        i += 1

    self.previousText = self.editArea.get('1.0', END)

  def search_re(self, pattern, text):
    matches = []
    text = text.splitlines()

    for i, line in enumerate(text):
      for match in re.finditer(pattern, line):

        matches.append(
          (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
        )

    return matches

  def add_tab(self, event):
    tabs=0
    back_line=(self.editArea.get('insert linestart','insert lineend'))
    for i in back_line:
      if i == ' ':
        tabs+=1
      else:
        break
    cut=' '*(tabs)
    self.editArea.insert('insert','\n')
    self.editArea.insert('insert',(cut))
    return 'break'

  def tab_pressed(self, event):
    self.editArea.insert(INSERT, " "*4)
    return "break"

  def new(self):
    self.editArea.delete("1.0", END)
    insert = """from random import randint

print([randint(1, 20) for i in range(10)])
"""
    self.editArea.insert(END, insert)
    self.changes()

  def save(self, event=None):
    try:
      picked = self.files.get(self.files.curselection()[0])
      path = os.path.join(self.current_path.get(), picked)
      with open(path, "w", encoding="utf-8") as f:
        f.write(self.editArea.get("1.0", END))
    except: showerror("Выберите файл для сохранения!", "Выберите файл в проводнике, в который хотите сохранить изменения!")
  
  def main(self):
    filemenu = Menu(self.menu, tearoff=0)
    filemenu.add_command(label="Новый", command=self.new)
    filemenu.add_command(label="Открыть...")
    filemenu.add_command(label="Сохранить", command=self.save)
    filemenu.add_command(label="Сохранить как...")
    filemenu.add_command(label="Выход", command=lambda: self.exit)
    
    self.menu.add_cascade(label="Файл", menu=filemenu)
    self.menu.add_command(label="Запуск", command=self.execute)

    #Проводник
    explorerFrame = Frame(self.main_frame, bg=self.background)
    explorerFrame.pack(fill=BOTH, side=LEFT)

    Label(explorerFrame, text="Проводник", font=self.font, fg=self.normal, bg=self.background).pack()

    btnsFrame = Frame(explorerFrame, bg=self.background)
    btnsFrame.pack()

    createFileBtn = btn(master=btnsFrame, text="+Файл", command=lambda: self.create('file'))
    createFileBtn.root.grid(column=0, row=0, padx=2)

    createFolderBtn = btn(master=btnsFrame, text="+Папка", command=lambda: self.create('folder'))
    createFolderBtn.root.grid(column=1, row=0, padx=2)

    self.files = Listbox(explorerFrame, bg="gray15", fg=self.normal, font=self.font, borderwidth=0, highlightthickness=0, selectbackground="gray30", height=25)
    self.files.pack()

    #Поле редактирования
    editAreaFrame = Frame(self.main_frame, bg="gray")
    editAreaFrame.pack(fill=BOTH, expand=1)

    self.editArea = Text(editAreaFrame, bg=self.background, fg=self.normal, insertbackground=self.normal, selectbackground="gray30", relief=FLAT, borderwidth=30, font=self.font)
    self.editArea.pack(fill=BOTH, expand=1)

    insert = """from random import randint

print([randint(1, 20) for i in range(10)])
"""

    self.editArea.insert('1.0', insert)

    self.editArea.bind('<KeyRelease>', self.changes)
    self.editArea.bind('<Return>', self.add_tab)
    self.editArea.bind('<Tab>', self.tab_pressed)
    self.editArea.bind('<Control-s>', self.save)

    self.main_frame.bind('<Control-r>', self.execute)
    self.main_frame.bind("<Alt-Left>", self.go_back)

    self.files.bind('<Double-1>', self.change_path_by_click)
    self.files.bind('<Return>', self.change_path_by_click)

    #Добавление цветов
    self.changes()
    #Выбор пути в проводнике
    self.path_change('')
