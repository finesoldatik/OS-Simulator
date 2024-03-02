from importlib import import_module
from os.path import dirname
from sys import argv

from res.modules.window import Window

if __name__ == "__main__":
  if len(argv) > 1: name = argv[1]
  else: name = "base"
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