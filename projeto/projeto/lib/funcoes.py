# funcoes.py
from dados import equipamentos, salas

# Funções CRUD para equipamentos
def cadastrar_equipamento(equipamento):
    equipamentos.append(equipamento)

def listar_equipamentos():
    return equipamentos

def atualizar_equipamento(index, novo_equipamento):
    equipamentos[index] = novo_equipamento

def deletar_equipamento(index):
    del equipamentos[index]

# Funções CRUD para salas
def cadastrar_sala(sala):
    salas.append(sala)

def listar_salas():
    return salas

def atualizar_sala(index, nova_sala):
    salas[index] = nova_sala

def deletar_sala(index):
    del salas[index]

# Funções para relatórios
def equipamentos_na_sala(sala):
    return [equipamento for equipamento in equipamentos if equipamento['sala'] == sala]

def relatorio_equipamentos():
    return equipamentos

def relatorio_salas():
    return salas
