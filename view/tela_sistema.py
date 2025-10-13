
class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Viagem em Grupo ---------")
        print("Escolha sua opcao")
        print("1 - Pessoas")
        print("2 - Grupos")
        print("3 - Local de viagem")
        print("4 - Passeio")
        print('5 - Passagem')
        print("6 - Pacote")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    