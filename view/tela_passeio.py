
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
        for passeio in passeios_dict:
            print(f'''{passeio['id']}. Atração: {passeio['atracao']}
                   Localização: {passeio['localizacao']}
                   Horário de início: {passeio['horario_inicio']}
                   Horário de fim: {passeio['horario_fim']}
                   Valor: {passeio['valor']}
                   Grupo do passeio: {passeio['grupo']}''')

    def seleciona_passeio(self):
        try:
            id_passeio = int(input("\nDigite o ID do passeio: "))
            return id_passeio
        except ValueError:
            self.mostra_mensagem("ID inválido!")
            return None

    def confirma_exclusao(self, atracao_turistica, nome_grupo):
        print(f"\nVocê confirma a exclusão do passeio turístico '{atracao_turistica}' do grupo '{nome_grupo}'?")

        while True:
            confirmacao = input("Digite 'S' para confirmar ou 'N' para cancelar: ").strip().upper()
            
            if confirmacao == 'S':
                return True
            elif confirmacao == 'N':
                return False
            else:
                print("Opção inválida! Digite 'S' para SIM ou 'N' para NÃO.")