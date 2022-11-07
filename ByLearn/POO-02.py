class Carro(object):
    estado = 'Novo'


fusca = Carro()
bmw = Carro()
ferrari = Carro()

print(f'fusca.estado: \n{fusca.estado}\nbmw.estado:\n{bmw.estado}\nferrari.estado:\n{ferrari.estado}\n\n')

fusca.estado = 'Usado'
bmw.estado = 'Semi-novo'


print('-'*5, 'Estados Atualizados:'.upper(), '-'*5)
print(f'fusca.estado: \n{fusca.estado}\nbmw.estado:\n{bmw.estado}\nferrari.estado:\n{ferrari.estado}')
