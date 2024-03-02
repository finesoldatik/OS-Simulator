from importlib import import_module

from res.modules.window import Window
from os import path

if __name__ == "__main__":
  name = "base"
  context = import_module(f"res.content.{name}.interface.context")
  desktop = import_module(f"res.content.{name}.interface.desktop")
  system_path = f"{path.dirname(__file__)}\\"
  win = Window(context=context.Context, desktop=desktop.Desktop, system_path=system_path)
  win.mainloop()