# Diferenciando atributos da classe com atributos de instancia
class Carro(object):
    estado = 'Novo'


carro1 = Carro()
print(f'Estado do carro1 antes de fazer modificações: {carro1.estado}')
carro1.estado = 'Semi-Novo'  # Neste momento, criamos um atributo de INSTANCIA
carro2 = Carro()

print(f'Estado do carro1 depois de fazer modificações: {carro1.estado}')
print(f'Estado atual do carro2: {carro2.estado}')

Carro.estado = 'Quebrado'
print(f'Novo valor de estado, na classe carro: {Carro.estado}')

carro3 = Carro()
# Carro 1 Possui um atributo de instancia, por tanto não é afetado pelas modificações na classe.
print(f'Estado do carro1 depois de fazer modificações na classe carro: {carro1.estado}')
# Carro 2 e 3 possui apenas o atributo de CLASSE, logo sempre que a classe for modificada, 
# seus atributos também serão ser modificados.
print(f'Estado do carro2 depois de fazer modificações na classe carro: {carro2.estado}')
print(f'estado de carro3 criado depois de fazer modificações na classe carro: {carro3.estado}')

