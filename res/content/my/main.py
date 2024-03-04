from tkinter import *

from res.modules.app import app

class App(app):
  def __init__(self, win, position, args=[]):
    super().__init__(win=win, position=position, title="MY TEST APP")
  
  def main(self):
    Label(self, text="MY_TEST_APP").pack()