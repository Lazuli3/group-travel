
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
        while True:
            atracao_turistica = input('Nome da atração turística: ')
            cidade = input('Cidade: ')
            pais = input('País: ')
            dia = input('Digite o dia (DD/MM/YYYY): ')
            horario_inicio = input('Digite o horário de início (HH:MM): ')
            horario_fim = input('Digite o horário de fim (HH:MM): ')
            valor = input('Digite o valor (R$): ')
            grupo_passeio = input('Digite o nome do grupo: ')

            if dt_fim <= dt_inicio:
                self.mostra_mensagem("Erro: horário de fim deve ser após o início!")
                continue

            return {
                '


