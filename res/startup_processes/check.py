from os.path import exists
from os import mkdir

class Process:
  def __init__(self, win):
    files = ["res\\tags.json"]
    folders = ["storage", "storage\\Documents", "storage\\Images", "storage\\Images\\Wallpapers", "storage\\Music"]
    for file in files:
      text = ""
      if not exists(file):
        if file.split(".")[1] == "json":
          text = "{}"
        with open(file, "w") as f:
          f.write(text)

    for folder in folders:
      if not exists(folder):
        mkdir(folder)