class Pilha:
    def __init__(self):
        self.items = []

    def getPilha(self):
        return self.items

    def isEmpty(self):
        return len(self.items) == 0

    def insert(self, numero):
        self.items.append(numero)

    def remove(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
