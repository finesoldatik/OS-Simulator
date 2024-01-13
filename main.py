# imports
from tkinter import *
from PIL import Image, ImageTk
from time import localtime, strftime
from importlib import import_module

from os import path, mkdir
system_path = path.dirname(__file__) + "\\"

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("psevdoOS")
        self.config(bg="gray10")
        self.wm_attributes("-fullscreen", 1)
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.opened_programs = []

        # colors
        self.normal = self.rgb((234, 234, 234))

        # fonts
        self.font = ('Consolas', 10, 'bold')

    def rgb(self, rgb): return "#%02x%02x%02x" % rgb

    def wallpaper(self, bg):
        wallpaper = Image.open(system_path + bg)
        wallpaper = wallpaper.resize((self.screenwidth, self.screenheight), Image.LANCZOS)
        wallpaper = ImageTk.PhotoImage(wallpaper)

        return wallpaper

    def get_prog(self, e):
        selection = e.widget.curselection()
        index = selection[0]
        self.config(menu=self.opened_programs[index].menu)

    def desktop(self):
        wallpaper = self.wallpaper("wallpapers\\2.jpg")
        self.wall = Label(win, image=wallpaper)
        self.wall.image = wallpaper
        self.wall.place(x=-2, y=-2)

        self.wall.bind("<Button-3>", self.do_popup)

        self.taskbar = Label(win, text="", bg='gray20', fg='white', font=self.font, width=10, height=self.screenheight)
        self.taskbar.place(x=0, y=0)

        self.programs = Listbox(self, width=12, height=int(self.screenheight / 18), borderwidth=0, bg="gray25", fg="white", selectbackground="gray25", highlightbackground="gray25")
        self.programs.place(x=1, y=36)

        self.programs.bind("<Button-1>", self.get_prog)

        self.system_time = Label(win, text='', bg='gray20', fg='white', font=self.font)
        self.system_time.place(x=0, y=0)

    def time_update(self):
        local = localtime()
        time_str = strftime("%H:%M:%S\n%d/%m/%Y", local)
        self.system_time.configure(text=time_str)
        win.after(1000, self.time_update)

    def loop(self):
        self.time_update()
        self.mainloop()

    def create_folder(self):
        mkdir("Storage/Новая папка")

    def create_document(self):
        with open("Storage/Documents/Новый документ.txt") as f: f.close()

    def create_image(self):
        with open("Storage/Images/Новое изображение.png") as f: f.close()

    def start_program(self, program: str):
        try:
            program = import_module(program)
            program = program.App(self)
            program.start()
            self.opened_programs.append(program)
            self.programs.insert(END, program.name["text"])
            self.config(menu=program.menu)
            return "started"
        except: return "err! program not found"

    def add_context(self):
        self.context = Menu(win, tearoff=0)
        create = Menu(self.context, tearoff=0)

        create.add_command(label="Папку", command=self.create_folder)
        create.add_command(label="Текстовый документ", command=self.create_document)
        create.add_command(label="Изображение", command=self.create_image)

        #self.context.add_command(label="Рисование", command=lambda: self.start_program("paint"))
        self.context.add_command(label="Блокнот", command=lambda: self.start_program("notepad"))
        #self.context.add_command(label="Проводник", command=lambda: self.start_program("explorer"))
        self.context.add_command(label="Калькулятор", command=lambda: self.start_program("calculator"))
        self.context.add_command(label="Терминал", command=lambda: self.start_program("terminal"))
        self.context.add_separator()
        self.context.add_cascade(label="Создать", menu=create)
        self.context.add_command(label="Выйти", command=quit)

    def do_popup(self, event):
        try: self.context.tk_popup(event.x_root, event.y_root)
        finally: self.context.grab_release()


if __name__ == "__main__":
    win = Window()
    win.desktop()
    win.add_context()
    win.loop()