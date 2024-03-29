from importlib import import_module
from os.path import dirname
from argparse import ArgumentParser

from src.window import Window

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-i", "--interface", dest="interface", type=str, help="The name of the interface that the program will run from.", default="base")
  args = parser.parse_args()
  package = args.interface
  print(f"\nlaunching with the \"{package}\" package.")
  try:
    context = import_module(f"res.content.{package}.interface.context")
    desktop = import_module(f"res.content.{package}.interface.desktop")
    system_path = f"{dirname(__file__)}\\"
    win = Window(context=context.Context, desktop=desktop.Desktop, system_path=system_path)
  except Exception as ex:
    print(f"\n----------------\t----------------\nerr! a package with that name was not found!\n{ex}\n\n----------------\t----------------\n")
  try:
    win.mainloop()
  except Exception as ex:
    print(ex)
  print("\nthe simulator is closed.\n")