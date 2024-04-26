from tkinter import *
from tkinter import colorchooser
from tkinter.messagebox import showinfo
from PIL import Image, ImageDraw
from random import randint

from res.api.app import app

class App(app):
  def __init__(self, win, position, args={}):
    self.brush_size = 10
    self.color = "black"
    self.x = 0
    self.y = 0
    super().__init__(win=win, position=position, title="Холст")

  def content(self):
    self.main_frame.columnconfigure(6, weight=1)
    self.main_frame.rowconfigure(2, weight=1)

    self.canvas = Canvas(self.main_frame, bg='white', width=1000, height=500)
    self.canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

    self.canvas.bind("<Button-1>", self.draw)
    self.canvas.bind('<B1-Motion>', self.draw)
    self.canvas.bind('<Button-3>', self.popup)

    self.context = Menu(self.main_frame, tearoff=0)
    self.context.add_command(label='Квадрат', command=self.square)
    self.context.add_command(label='Круг', command=self.circle)
    self.image = Image.new('RGB', (1000, 500), 'white')
    self.draw_img = ImageDraw.Draw(self.image)

    Label(self.main_frame, text='Параметры: ').grid(row=0, column=0, padx=6)

    Button(self.main_frame, text='Выбрать цвет', width=11, command=self.chooseColor).grid(row=0, column=1, padx=6)

    self.color_lab = Label(self.main_frame, bg="black", width=10)
    self.color_lab.grid(row=0, column=2, padx=6)

    v = IntVar(value=10)
    Scale(self.main_frame, variable=v, from_=1, to=100, orient=HORIZONTAL, command=self.select).grid(row=0, column=3, padx=6)

    Label(self.main_frame, text='Действия: ').grid(row=1, column=0, padx=6)

    Button(self.main_frame, text='Заливка', width=10, command=self.pour).grid(row=1, column=1)

    Button(self.main_frame, text='Очистить', width=10, command=self.clear_canvas).grid(row=1, column=2)

    Button(self.main_frame, text='Сохранить', width=10, command=self.save_img).grid(row=1, column=6)

  def draw(self, event):
    x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
    x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
    self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=0)
    self.draw_img.ellipse((x1, y1, x2, y2), fill=self.color, width=0)

  def chooseColor(self):
    (rgb, hx) = colorchooser.askcolor()
    self.color = hx
    self.color_lab.configure(bg=hx)

  def select(self, value):
    self.brush_size = int(value)

  def pour(self):
    self.canvas.delete('all')
    self.canvas.configure(bg=self.color)
    self.draw_img.rectangle((0, 0, 1000, 500), width=0, fill=self.color)

  def clear_canvas(self):
    self.canvas.delete('all')
    self.canvas.configure(bg='white')
    self.draw_img.rectangle((0, 0, 1000, 500), width=0, fill='white')

  def save_img(self):
    filename = f'Storage/Local/Images/image_{randint(0, 10000)}.png'
    self.image.save(filename)
    showinfo('Cохранение', 'Сохранено под названием %s' % filename)

  def popup(self, event):
    self.x, self.y = event.x, event.y
    self.context.post(event.x_root, event.y_root)

  def square(self):
    self.canvas.create_rectangle(self.x - self.brush_size, self.y - self.brush_size, self.x + self.brush_size, self.y + self.brush_size, fill=self.color, width=0)
    self.draw_img.polygon((self.x, self.y, self.x + self.brush_size, self.y, self.x + self.brush_size, self.y + self.brush_size, self.x, self.y + self.brush_size), fill=self.color)

  def circle(self):
    self.canvas.create_oval(self.x - self.brush_size, self.y - self.brush_size, self.x + self.brush_size, self.y + self.brush_size, fill=self.color, width=0)
    self.draw_img.ellipse((self.x, self.y, self.x + self.brush_size, self.y + self.brush_size), fill=self.color)