
class TelaLocalViagem:

    def mostra_mensagem(self, msg:str):
        print(msg)
    
    def mostra_opcoes(self):
        '''
            ============ Menu ============')
            1 - Incluir local de viagem")
            2 - Listar local de viagem')
            3 - Excluir local de viagem')
            0 - Sair
        '''

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
    
    def lista_locais_viagem(self, locais_viagem:list):
        if not locais_viagem:
            self.mostra_mensagem("Nenhum local foi cadastrado.")
        
        print('============ Lista de locais ============')
        for {i}, local in enumerate(locais_viagem, 1):
            print(f"Cidade: {local.cidade} | País: {local.pais}")
