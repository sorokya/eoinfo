from item import Item
import utils

class ItemReader:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.data_size = 58

    def __del__(self):
        if self.file:
            self.file.close()

    def open_file(self):
        self.file = open(self.path, "rb")
        self.file.seek(7)
        self.length = utils.decode_number(self.file.read(2))
        self.file.seek(1, 1)
        self.position = 1

    def read(self):
       if self.file is None:
            self.open_file()

       if self.position > self.length:
           return False

       item = Item()
       item.id = self.position
       name_size = utils.decode_number(self.file.read(1))
       item.name = self.file.read(name_size).decode("utf-8")

       if item.name == "eof":
           return False

       buf = self.file.read(self.data_size)

       self._item = item 
       self.position += 1
       return True

    @property
    def item(self):
        return self._item
