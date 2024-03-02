from json import dumps, loads
from os import listdir
from importlib import import_module
from tkinter import *


class JsonHandler:
  """Обработчик JSON."""
  def write(path:str, data:dict):
    """Запись данных в json файл."""
    with open(path, 'w', encoding='utf-8') as f:
      f.write(dumps(data, indent=4, ensure_ascii=False))


  def read(path:str) -> dict:
    """Чтение данных из json файла."""
    with open(path, 'r', encoding='utf-8') as f:
      data = loads(f.read())
    return data

class ProcessHandler:
  """Обработчик Процессов."""
  def run_startup(win):
    """Запуск стартовых процессов"""
    startup_processes = listdir("res\\startup_processes")
    for process in startup_processes:
      if process == "__pycache__":
        continue
      process = process.split(".")[0]
      process = import_module(f"res.startup_processes.{process}")
      process.Process(win)

  def start(win, process_import_path:str) -> str:
    """Запуск процесса по его пути импорта."""
    try:
      process = import_module(process_import_path)
      process.Process(win)
      return "started!"
    except: return "err! process not found!"

class ProgramHandler:
  def __init__(self, win, opened_programs, programs):
    self.opened_programs = opened_programs
    self.programs = programs
    self.win = win

  def start(self, program_import_path:str, args:list=None) -> str:
    """Запуск программы по её пути импорта."""
    try:
      program = import_module(f"res.content.{program_import_path}")
      program = program.App(self.win, args)
      self.opened_programs.append(program)
      self.programs.insert(END, program.name["text"])
      return "started!"
    except: return "err! program not found!"