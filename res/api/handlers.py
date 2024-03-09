"""
Модуль handlers помогает обрабатывать JSON,
    приложения и процессы симулятора ОС.

finesoldatik
finesoldat@gmail.com
# License: MIT
"""
__author__ = 'finesoldatik'

__version__ = "0.0.1"

from json import dumps, loads
from os import listdir
from importlib import import_module
from tkinter import *

class JSONHandler:
  """Класс JSONHandler облегчает получение данных из JSON файлов

    Основное применение - получение данных из JSON файлов

    Methods
    -------
    write(path: str, data: dict)
        записывает данные в JSON файл
    read(path: str) -> dict
        читает и возвращает данные из JSON файла
  """
  def write(path: str, data: dict):
    """Записывает данные в JSON файл.

      Parameters
      ----------
      path : str
          путь до файла
      data : dict
          данные, записываемые в файл
    """
    with open(path, 'w', encoding='utf-8') as f:
      f.write(dumps(data, indent=4, ensure_ascii=False))


  def read(path: str) -> dict:
    """Читает и возвращает данные из JSON файла.

      Parameters
      ----------
      path : str
          путь до файла
    """
    with open(path, 'r', encoding='utf-8') as f:
      data = loads(f.read())
    return data

class ProcessHandler:
  """Класс ProcessHandler запускает процессы симулятора ОС

    Основное применение - запуск процессов симулятора ОС

    Methods
    -------
    run_startup(win: Window)
        запускает стартовые процессы
            (выполняется по умолчанию при запуске симулятора ОС)
    start(win: Window, process_import_path: str) -> str
        запускает процесс и возвращает код запуска
  """
  def run_startup(win):
    """Запускает стартовые процессы.

      Parameters
      ----------
      win : Window
          окно симулятора ОС
    """
    startup_processes = listdir("res\\startup_processes")
    for process in startup_processes:
      if process == "__pycache__":
        continue
      process = process.split(".")[0]
      process = import_module(f"res.startup_processes.{process}")
      process.Process(win)

  def start(win, process_import_path: str) -> str:
    """Запускает процесс.

      Parameters
      ----------
      win : Window
          окно симулятора ОС
      process_import_path : str
          путь импорта процесса
    """
    try:
      process = import_module(process_import_path)
      process.Process(win)
      return "started!"
    except Exception as ex:
      print("err!", ex)
      return "err! process not found!"

class ProgramHandler:
  """Класс ProgramHandler запускает приложения симулятора ОС

    Основное применение - запуск приложений симулятора ОС

    Attributes
    ----------
    win : Window
        окно симулятора ОС
    opened_programs : list
        список открытых приложений
    programslist : Listbox
        листбокс панели задач с открытыми приложениями

    Methods
    -------
    start(win: Window, process_import_path: str) -> str
        запускает приложение и возвращает код запуска
  """
  def __init__(self, win, opened_programs: list, programslist: Listbox):
    self.win = win
    self.opened_programs = opened_programs
    self.programslist = programslist

  def start(self, program_import_path:str, args:dict={}, position=[CENTER, CENTER]) -> str:
    """Запускает процесс.

      Parameters
      ----------
      win : Window
          окно симулятора ОС
      program_import_path : str
          путь импорта приложения
      args : dict={}
          аргументы приложения
    """
    try:
      program = import_module(f"res.content.{program_import_path}") # импортирует программу
      program = program.App(win=self.win, args=args, position=position) # вызывает класс из импорта
      self.opened_programs.append(program) # добавляет в список открытых программ
      self.programslist.insert(END, program.title["text"]) # добавляет в листбокс с программами
      return "started!"
    except Exception as ex:
      print("err!", ex)
      return "err! program not found!"
