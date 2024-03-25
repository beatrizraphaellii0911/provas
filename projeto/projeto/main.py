# main.py
from lib.funcoes import *

def menu():
    print("=== MENU ===")
    print("1. Cadastrar Equipamento")
    print("2. Listar Equipamentos")
    print("3. Atualizar Equipamento")
    print("4. Deletar Equipamento")
    print("5. Cadastrar Sala")
    print("6. Listar Salas")
    print("7. Atualizar Sala")
    print("8. Deletar Sala")
    print("9. Emitir Relatório de Equipamentos na Sala")
    print("10. Emitir Relatório de Todos os Equipamentos")
    print("11. Emitir Relatório de Todas as Salas")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            equipamento = {'nome': input("Nome do equipamento: "), 'sala': input("Sala do equipamento: ")}
            cadastrar_equipamento(equipamento)
        elif opcao == '2':
            print(listar_equipamentos())
        elif opcao == '3':
            index = int(input("Índice do equipamento a ser atualizado: "))
            novo_equipamento = {'nome': input("Novo nome do equipamento: "), 'sala': input("Nova sala do equipamento: ")}
            atualizar_equipamento(index, novo_equipamento)
        elif opcao == '4':
            index = int(input("Índice do equipamento a ser deletado: "))
            deletar_equipamento(index)
        elif opcao == '5':
            sala = input("Nome da sala: ")
            cadastrar_sala(sala)
        elif opcao == '6':
            print(listar_salas())
        elif opcao == '7':
            index = int(input("Índice da sala a ser atualizada: "))
            nova_sala = input("Novo nome da sala: ")
            atualizar_sala(index, nova_sala)
        elif opcao == '8':
            index = int(input("Índice da sala a ser deletada: "))
            deletar_sala(index)
        elif opcao == '9':
            sala = input("Nome da sala para emitir o relatório: ")
            print(equipamentos_na_sala(sala))
        elif opcao == '10':
            print(relatorio_equipamentos())
        elif opcao == '11':
            print(relatorio_salas())
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
