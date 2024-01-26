# импорт модулей
from tkinter import *
from PIL import Image, ImageTk
from time import localtime, strftime
from importlib import import_module

from os import path, mkdir, listdir
system_path = f"{path.dirname(__file__)}\\"

# импорт локальных модулей
from modules.json_handler import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("psevdoOS")
        self.config(bg="gray10")
        self.wm_attributes("-fullscreen", 1)
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.opened_programs = []

        # цвета
        self.normal = self.rgb((234, 234, 234))

        # шрифты
        self.font = ('Consolas', 10, 'bold')

        # контекстное меню
        self.context = Menu(self, tearoff=0)
        self.create = Menu(self.context, tearoff=0)
        self.base_programs = Menu(self.context, tearoff=0)
        self.taskmenu = Menu(self.context, tearoff=0)

        # запуск необходимых процессов для запуска
        self.run_startup_processes()

    def run_startup_processes(self):
        startup_processes = listdir("startup_processes")
        for process in startup_processes:
            if process == "__pycache__":
                continue
            process = process.split(".")[0]
            process = import_module(f"startup_processes.{process}")
            process.Process(self)

    def start_process(self, process_import_path:str) -> str:
        """Запуск процесса по его пути импорта."""
        try:
            process = import_module(process_import_path)
            process.Process(self)
            return "started!"
        except: return "err! process not found!"

    def rgb(self, rgb): return "#%02x%02x%02x" % rgb

    def wallpaper(self, bg):
        wallpaper = Image.open(system_path + bg)
        wallpaper = wallpaper.resize((self.screenwidth, self.screenheight), Image.LANCZOS)
        wallpaper = ImageTk.PhotoImage(wallpaper)

        return wallpaper

    def get_prog(self, e):
        selection = e.widget.curselection()
        if len(selection) > 0:
            index = selection[0]
            self.config(menu=self.opened_programs[index].menu)

    def hide_taskbar(self): self.taskbar.place_forget()
    def view_taskbar(self): self.taskbar.place(x=0, y=0)

    def desktop(self):
        wallpaper = self.wallpaper("wallpapers\\2.jpg")
        self.wall = Label(self, image=wallpaper)
        self.wall.image = wallpaper
        self.wall.place(x=-2, y=-2)

        self.wall.bind("<Button-3>", self.do_popup)

        self.taskbar = Frame(self, background="gray20")
        self.taskbar.place(x=0, y=0)

        self.system_time = Label(self.taskbar, text='', bg='gray20', fg='white', font=self.font)
        self.system_time.grid(column=0, row=0)

        self.programs = Listbox(self.taskbar, width=12, height=30, borderwidth=0, bg="gray25", fg="white", selectbackground="gray25", highlightbackground="gray25")
        self.programs.grid(column=0, row=1, pady=1)

        self.programs.bind("<Button-1>", self.get_prog)

        self.time_update()

    def time_update(self):
        local = localtime()
        time_str = strftime("%H:%M:%S\n%d/%m/%Y", local)
        self.system_time.configure(text=time_str)
        win.after(1000, self.time_update)

    def create_folder(self, path_=""):
        mkdir(f"Storage/{path_}Новая папка")

    def create_document(self):
        with open("Storage/Documents/Новый документ.txt") as f: f.close()

    def create_image(self):
        with open("Storage/Images/Новое изображение.png") as f: f.close()

    def start_program(self, program_import_path:str) -> str:
        """Запуск программы по её пути импорта"""
        try:
            program = import_module(program_import_path)
            program = program.App(self)
            self.opened_programs.append(program)
            self.programs.insert(END, program.name["text"])
            return "started!"
        except: return "err! program not found!"

    def add_context(self):
        self.base_programs.add_command(label="Холст", command=lambda: self.start_program("base.paint"))
        self.base_programs.add_command(label="Блокнот", command=lambda: self.start_program("base.notepad"))
        self.base_programs.add_command(label="Проводник", command=lambda: self.start_program("base.explorer"))
        self.base_programs.add_command(label="Калькулятор", command=lambda: self.start_program("base.calculator"))
        self.base_programs.add_command(label="Терминал", command=lambda: self.start_program("base.terminal"))

        self.create.add_command(label="Папку", command=self.create_folder)
        self.create.add_command(label="Текстовый документ", command=self.create_document)
        self.create.add_command(label="Изображение", command=self.create_image)

        self.taskmenu.add_command(label="Скрыть", command=self.hide_taskbar)
        self.taskmenu.add_command(label="Показать", command=self.view_taskbar)

        self.context.add_cascade(label="Открыть", menu=self.base_programs)
        self.context.add_cascade(label="Создать", menu=self.create)
        self.context.add_cascade(label="Панель задач", menu=self.taskmenu)
        self.context.add_separator()
        self.context.add_command(label="Выйти", command=quit)

    def do_popup(self, event):
        try: self.context.tk_popup(event.x_root, event.y_root)
        finally: self.context.grab_release()


if __name__ == "__main__":
    win = Window()
    win.desktop()
    win.add_context()
    win.mainloop()
