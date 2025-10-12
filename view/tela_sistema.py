
class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisLivros ---------")
        print("Escolha sua opcao")
        print("1 - Pessoas")
        print("2 - Grupos")
        print("3 - Local de viagem")
        print("4 - Passagem")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao