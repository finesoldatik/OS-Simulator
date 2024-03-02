from os.path import exists

class Process:
    def __init__(self, win):
        files = ["res\\tags.json"]
        for file in files:
            text = ""
            if not exists(file):
                if file.split(".")[1] == "json": text = "{}"
                with open(file, "w") as f: f.write(text)
