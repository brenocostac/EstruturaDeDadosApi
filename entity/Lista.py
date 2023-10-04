class Lista:
    def __init__(self):
        self.items = []

    def getLista(self):
        return self.items

    def isEmpty(self):
        return len(self.items) == 0

    def insert(self, numero):
        self.items.append(numero)

    def remove(self, numero):
        if not self.isEmpty():
            return self.items.remove(numero)
        return None
