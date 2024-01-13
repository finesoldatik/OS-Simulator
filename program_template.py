from tkinter import *

class App:
    def __init__(self, win):
        self.win = win
        self.font = ('Consolas', 10, 'bold')

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

        self.name = Label(self.topframe, text='Программа', width=30)
        self.name.grid(column=0, row=0)

        Button(self.topframe, text='X', bg='red', fg='white', font=self.font, border=0, width=3, command=self.quit).grid(column=1, row=0)

        self.prog = Frame(self.top)
        self.prog.grid(column=0, row=1)
        self.name.bind('<B1-Motion>', self.move_app)
        self.program()

    def program(self):

        # end
        self.menu = Menu(self.prog, tearoff=0)
        self.menu.add_command(label="Центрировать", command=self.center)
        self.menu.add_command(label="Закрыть", command=self.quit)
        self.win.update_idletasks()
        self.width = self.top.winfo_width() * 2
        self.height = self.top.winfo_height() / 1.6

    def move_app(self, e):
        self.top.place(x=e.x_root - self.width, y=e.y_root - self.height)
        self.win.config(menu=self.menu)