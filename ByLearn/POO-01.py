class Carro(object):
    estado = 'Novo'


fusca = Carro()
fusca.estado = 'Usado'
ferrari = Carro()
ferrari.estado = 'Novo'

print(f'Estado do fusca: \n{fusca.estado}\n')
print(f'Tipo de fusca: \n{type(fusca)}\n')
print(f'Tipo de fusca.estado: \n{type(fusca.estado)}\n')
print(f'Estado da ferrari: \n{ferrari.estado}\n')
print(f'Tipo de ferrari: \n{type(ferrari)}\n')
print(f'Tipo de ferrari.estado: \n{type(ferrari.estado)}\n')
