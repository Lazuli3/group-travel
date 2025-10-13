
class TelaPasseioTuristico:
    def mostra_mensagem(self, msg:str):
        print(msg)

    def mostra_opcoes(self):
        while True:
            print('''============ Menu ============
                1 - Incluir passeio turístico
                2 - Listar passeios turísticos
                3 - Excluir passeio turístico
                0 - Sair
            ''')

            try:
                return int(input('Escolha uma das opções do menu: '))
            
            except ValueError:
                self.mostra_mensagem('Escolha uma opção válida do menu.')

    def pega_dados_passeio(self):
        print('\n============ Cadastro ============')
        atracao_turistica = input('Nome da atração turística: ')
        cidade = input('Cidade: ')
        pais = input('País: ')
        dia = input('Digite o dia (DD/MM/YYYY): ')
        horario_inicio = input('Digite o horário de início (HH:MM): ')
        horario_fim = input('Digite o horário de fim (HH:MM): ')
        valor = input('Digite o valor (R$): ')
        id_grupo = input('Digite o ID do grupo: ')

        return {
            'atracao_turistica': atracao_turistica,
            'cidade': cidade,
            'pais': pais,
            'dia': dia,
            'horario_inicio': horario_inicio,
            'horario_fim': horario_fim,
            'valor': valor,
            'id_grupo': id_grupo
        }

    def lista_passeios_turisticos(self, passeios_dict: list):
        print('============ Lista de passeios ============')
        for i, passeio in enumerate(passeios_dict, 1):
            print(f'''{i}. Atração: {passeio['atracao']}
                   Localização: {passeio['localizacao']}
                   Horário de início: {passeio['horario_inicio']}
                   Horário de fim: {passeio['horario_fim']}
                   Valor: {passeio['valor']}
                   Grupo do passeio: {passeio['grupo']}''')

    def seleciona_passeio(self, passeios_dict: list):
        if not passeios_dict:
            self.mostra_mensagem("Nenhum passeio disponível para seleção.")
            return None

        self.lista_passeios_turisticos(passeios_dict)

        while True:
            try:
                opcao = int(input('\nDigite o número do passeio ou 0 para cancelar.'))

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(passeios_dict):
                    return opcao - 1 #índice real e ajustado
                else:
                    self.mostra_mensagem(
                        f'Digite um número entre 1 e {len(passeios_dict)}.'
                    )

            except ValueError:
                self.mostra_mensagem('Digite um número válido.')
