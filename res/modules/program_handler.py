from importlib import import_module
from tkinter import *

class ProgramHandler:
  def __init__(self, win, opened_programs, programs):
    self.opened_programs = opened_programs
    self.programs = programs
    self.win = win

  def start(self, program_import_path:str, args:list=None) -> str:
    """Запуск программы по её пути импорта"""
    try:
      program = import_module(f"res.content.{program_import_path}")
      program = program.App(self.win, args)
      self.opened_programs.append(program)
      self.programs.insert(END, program.name["text"])
      return "started!"
    except: return "err! program not found!"
