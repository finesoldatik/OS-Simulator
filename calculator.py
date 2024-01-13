from tkinter import *

class App:
    def __init__(self, win):
        self.win = win
        self.font = ('Consolas', 10, 'bold')
        self.expression = ""

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

        self.name = Label(self.topframe, text='Калькулятор', width=35)
        self.name.grid(column=0, row=0)

        Button(self.topframe, text='X', bg='red', fg='white', font=self.font, border=0, width=3, command=self.quit).grid(column=1, row=0)

        self.prog = Frame(self.top)
        self.prog.grid(column=0, row=1)
        self.name.bind('<B1-Motion>', self.move_app)
        self.program()

    def btn_click(self, item):
        try:
            self.input_field['state'] = "normal"
            self.expression += item
            self.input_field.insert(END, item)

            if item == '=':
                result = str(eval(self.expression[:-1]))
                self.input_field.delete('0', END)
                self.input_field.insert(END, result)
                expression = ""
            self.input_field['state'] = "readonly"

        except ZeroDivisionError:
            self.input_field.delete(0, END)
            self.input_field.insert(0, 'Ошибка (деление на 0)')
        except SyntaxError:
            self.input_field.delete(0, END)
            self.input_field.insert(0, 'Ошибка')

    def bt_clear(self):
        self.expression = ""
        self.input_field['state'] = "normal"
        self.input_field.delete(0, END)
        self.input_field['state'] = "readonly"

    def program(self):
        frame_input = Frame(self.prog)
        frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")

        self.input_field.pack(fill=BOTH)

        buttons = (('7', '8', '9', '/'),
                   ('4', '5', '6', '*'),
                   ('1', '2', '3', '-'),
                   ('0', '.', '=', '+'))

        button = Button(self.prog, text='C', command=lambda: self.bt_clear())
        button.grid(row=1, column=3, sticky="nsew")
        for ro in range(4):
            for co in range(4):
                Button(self.prog, width=2, height=3, text=buttons[ro][co], command=lambda row=ro, col=co: self.btn_click(buttons[row][col])).grid(row=ro + 2, column=co, sticky="nsew", padx=1, pady=1)
        # end
        self.menu = Menu(self.prog, tearoff=0)
        self.menu.add_command(label="Центрировать", command=self.center)
        self.menu.add_command(label="Закрыть", command=self.quit)
        self.win.update_idletasks()
        self.width = self.top.winfo_width() * 3.3
        self.height = self.top.winfo_height() * 1.35

    def move_app(self, e):
        self.top.place(x=e.x_root - self.width, y=e.y_root - self.height)
        self.win.config(menu=self.menu)