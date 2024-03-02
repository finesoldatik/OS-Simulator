from json import dumps, loads

class JsonHandler:
  def write(path:str, data:dict):
    """Запись данных в json файл"""
    with open(path, 'w', encoding='utf-8') as f:
      f.write(dumps(data, indent=4, ensure_ascii=False))


  def read(path:str) -> dict:
    """Чтение данных из json файла"""
    with open(path, 'r', encoding='utf-8') as f:
      data = loads(f.read())
    return data
