from os import listdir
from importlib import import_module

class ProcessHandler:
  def run_startup(win):
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