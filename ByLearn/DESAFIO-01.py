# Criar uma classe carro onde além de estado também tem um nome por padrão
# (Construtor), e um método que ira printar o nome e estado do carro

class Carro(object):
    def __init__(self, estado, nome):
        self.estado = estado
        self.nome = nome

    def mostrar_informacoes(self):
        print(f'O carro {self.nome} tem o estado {self.estado}')


bmw = Carro('Semi-Novo', 'bmw')
ferrari = Carro('Novo', 'Ferrari')
fusca = Carro(nome='Fusca', estado='Usado')

bmw.mostrar_informacoes()
ferrari.mostrar_informacoes()
fusca.mostrar_informacoes()
