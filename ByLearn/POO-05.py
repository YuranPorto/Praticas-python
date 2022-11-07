# Construtor de classes
class Carro(object):
    def __init__(self, estado):
        self.estado = estado


bmw = Carro('Semi-novo')
ferrari = Carro('Novo')
fusca = Carro('Usado')
print(f'bmw.estado: {bmw.estado}')
print(f'ferrari.estado: {ferrari.estado}')
print(f'fusca.estado: {fusca.estado}')
