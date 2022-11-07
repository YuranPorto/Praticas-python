class Carro(object):
    estado = 'Novo'

    def dirigir(self):
        self.estado = 'Usado'

# Exemplo 1


bmw = Carro()  # Ao criar o objeto, ele cria com o estado padrão, definido na classe
print(f'Estado da BMW Antes de ser dirigida: {bmw.estado}')
bmw.dirigir()  # Modifica o estado apenas na instancia
print(f'Estado da BMW Após ser dirigida: {bmw.estado}')
