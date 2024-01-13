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

        self.name = Label(self.topframe, text='Терминал', width=14)
        self.name.grid(column=0, row=0)

        Button(self.topframe, text='X', bg='red', fg='white', font=self.font, border=0, width=3, command=self.quit).grid(column=1, row=0)

        self.prog = Frame(self.top)
        self.prog.grid(column=0, row=1)
        self.name.bind('<B1-Motion>', self.move_app)
        self.program()

    def cmd(self, e):
        cmd = self.entry.get()
        cmd = cmd.lower()
        if cmd not in ["", " ", "  ", "   "]:
            cmd = cmd.split()
            if len(cmd) > 1:
                if cmd[0] == "start": output = self.win.start_program(cmd[1])
                self.output.config(text=output)
            else:
                if cmd[0] == "oprogs":
                    programs = ""
                    for program in self.win.opened_programs:
                        programs += f"{program.name['text']}\n"
                    output = programs
                self.output.config(text=output)

    def program(self):
        self.output = Label(self.prog)
        self.output.pack()
        self.entry = Entry(self.prog)
        self.entry.pack()
        self.entry.bind("<Return>", self.cmd)

        # end
        self.menu = Menu(self.prog, tearoff=0)
        self.menu.add_command(label="Центрировать", command=self.center)
        self.menu.add_command(label="Закрыть", command=self.quit)
        self.win.update_idletasks()
        self.width = self.top.winfo_width() * 7
        self.height = self.top.winfo_height() * 8.7

    def move_app(self, e):
        self.top.place(x=e.x_root - self.width, y=e.y_root - self.height)
        self.win.config(menu=self.menu)