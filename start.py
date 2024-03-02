from importlib import import_module
from os.path import dirname
from argparse import ArgumentParser

from res.modules.window import Window

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-i", "--interface", dest="interface", type=str, help="The name of the interface that the program will run from.", default="base")
  args = parser.parse_args()
  name = args.interface
  print(f"\nlaunching with the \"{name}\" package.")
  try:
    context = import_module(f"res.content.{name}.interface.context")
    desktop = import_module(f"res.content.{name}.interface.desktop")
    system_path = f"{dirname(__file__)}\\"
    win = Window(context=context.Context, desktop=desktop.Desktop, system_path=system_path)
  except: print("\n----------------\t----------------\nerr! a package with that name was not found!\n----------------\t----------------\n")
  try: win.mainloop()
  except: pass
  print("\nthe program is closed.\n")