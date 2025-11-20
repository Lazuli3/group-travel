
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
            print(f"{local['id']}. Cidade: {local['cidade']} | País: {local['pais']}")

    def seleciona_local(self):
        try:
            id_local = int(input("\nDigite o ID do local: "))
            return id_local
        except ValueError:
            self.mostra_mensagem("ID inválido!")
            return None

    def confirma_exclusao(self, cidade_local, pais_local):
        print(f"\nVocê confirma a exclusão do local de viagem: '{cidade_local}, {pais_local}'?")
        resposta = input("Certeza que quer excluir? (S/N): ").strip().upper()
        return resposta == 'S'