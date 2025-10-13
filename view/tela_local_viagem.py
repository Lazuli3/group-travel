
class TelaLocalViagem:

    def mostra_mensagem(self, msg: str):
        print(msg)

    def mostra_opcoes(self):
        print(''' ============ Menu ============
            1 - Incluir local de viagem
            2 - Listar local de viagem
            3 - Excluir local de viagem
            0 - Sair
        ''')

        try:
            return int(input('Escolha uma das opções do menu: '))
        
        except ValueError:
            self.mostra_mensagem("Escolha uma opção válida do menu.")
            return self.mostra_opcoes()

    def pega_dados_local_viagem(self):
        print('============ Cadastro ============')
        cidade = input('Nome da cidade: ')
        pais = input('Nome do país: ')
        return {
            'cidade': cidade,
            'pais': pais
        }

    def lista_locais_viagem(self, locais_dict: list):
        print('============ Lista de locais ============')
        for i, local in enumerate(locais_dict, 1):
            print(f"{i}. Cidade: {local.cidade} | País: {local.pais}")

    def seleciona_local(self, locais_viagem: list):
        self.lista_locais_viagem(locais_viagem)

        while True:
            try:
                opcao = int(input("\nDigite o número do local ou 0 para cancelar: "))

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(locais_viagem):
                    return opcao - 1  #índice ajustado
                else:
                    self.mostra_mensagem(
                        f"Digite um número entre 1 e {len(locais_viagem)}."
                    )

            except ValueError:
                self.mostra_mensagem("Digite um número válido.")
