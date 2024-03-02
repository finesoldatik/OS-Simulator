from tkinter import *

from res.modules.app import app


class App(app):
    def __init__(self, win, args):
        super().__init__(win, "main", "Калькулятор")
        self.set_size(30, 20.3)
        self.expression = ""

    def btn_click(self, item):
        try:
            self.input_field['state'] = "normal"
            self.expression += item
            self.input_field.insert(END, item)

            if item == '=':
                result = str(eval(self.expression[:-1]))
                self.input_field.delete('0', END)
                self.input_field.insert(END, result)
                self.expression = ""
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

    def main(self):
        frame_input = Frame(self.main_frame)
        frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")

        self.input_field.pack(fill=BOTH)

        buttons = (('7', '8', '9', '/'),
                   ('4', '5', '6', '*'),
                   ('1', '2', '3', '-'),
                   ('0', '.', '=', '+'))

        button = Button(self.main_frame, text='C', command=lambda: self.bt_clear())
        button.grid(row=1, column=3, sticky="nsew")
        for ro in range(4):
            for co in range(4):
                Button(self.main_frame, width=2, height=3, text=buttons[ro][co], command=lambda row=ro, col=co: self.btn_click(buttons[row][col])).grid(row=ro + 2, column=co, sticky="nsew", padx=1, pady=1)
        self.add_menu()
