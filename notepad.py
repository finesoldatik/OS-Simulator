from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfile, askopenfile

class App:
    def __init__(self, win):
        self.win = win
        self.font = ('Consolas', 10, 'bold')
        self.filename = NONE

    def quit(self):
        self.win.programs.delete(self.win.opened_programs.index(self))
        self.win.opened_programs.remove(self)
        self.top.destroy()

    def center(self):
        self.top.place(x=200, y=200)

    def start(self):
        self.top = Frame(self.win, width=570, height=190)
        self.top.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.topframe = Frame(self.top)
        self.topframe.grid(column=0, row=0)

        self.name = Label(self.topframe, text='Блокнот', width=55)
        self.name.grid(column=0, row=0)

        Button(self.topframe, text='X', bg='red', fg='white', font=self.font, border=0, width=3, command=self.quit).grid(column=1, row=0)

        self.prog = Frame(self.top)
        self.prog.grid(column=0, row=1)
        self.name.bind('<B1-Motion>', self.move_app)
        self.program()

    def move_app(self, e):
        self.top.place(x=e.x_root - self.width, y=e.y_root - self.height)
        self.win.config(menu=self.menu)

    def new_file(self):
        self.filename = "Untitled"
        self.text.delete('1.0', END)

    def save_file(self):
        data = self.text.get('1.0', END)
        with open(f"Storage/Documents/{self.filename}.txt", 'w') as f:
            f.write(data)
            f.close()

    def save_as(self):
        out = asksaveasfile(mode='w', defaultextension='txt')
        data = self.text.get('1.0', END)
        try:
            out.write(data.rstrip())
        except Exception:
            showerror(title="Error", message="Saving file error")

    def open_file(self):
        inp = askopenfile(mode="r")
        if inp is None:
            return
        self.filename = inp.name
        data = inp.read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', data)

    def program(self):
        self.text = Text(self.prog, width=50, height=30, wrap="word")
        scrollb = Scrollbar(self.prog, orient=VERTICAL, command=self.text.yview)
        scrollb.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=scrollb.set)

        self.text.pack()
        self.menu = Menu(self.prog, tearoff=0)
        fileMenu = Menu(self.menu, tearoff=0)
        fileMenu.add_command(label="Новый", command=self.new_file)
        fileMenu.add_command(label="Открыть", command=self.open_file)
        fileMenu.add_command(label="Сохранить", command=self.save_file)
        fileMenu.add_command(label="Сохранить как", command=self.save_as)
        self.menu.add_cascade(label="Файл", menu=fileMenu)
        self.menu.add_command(label="Центрировать", command=self.center)
        self.menu.add_command(label="Закрыть", command=self.quit)
        self.win.config(menu=self.menu)
        self.win.update_idletasks()
        self.width = self.top.winfo_width() * 2
        self.height = self.top.winfo_height() / 1.6
