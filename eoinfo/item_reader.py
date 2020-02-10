from item import Item

class ItemReader:
    def __init__(self, path):
        self.path = path
        self.file = None

    def __del__(self):
        if self.file:
            self.file.close()

    def read(self):
       if self.file is None:
           self.file = open(self.path)

       self._item = Item()
       return True

    @property
    def item(self):
        return self._item
