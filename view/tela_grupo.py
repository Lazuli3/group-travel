import FreeSimpleGUI as sg

class TelaGrupo:

    def mostra_opcoes(self):
        layout = [
            [sg.Text('============ Menu ============')],
            [sg.Button('1 - Criar grupo')],
            [sg.Button('2 - Listar grupo')],
            [sg.Button('3 - Adicionar membro ao grupo')],
            [sg.Button('4 - Listar membros do grupo')],
            [sg.Button('5 - Remover membros do grupo')],
            [sg.Button('6 - Excluir grupo')],
            [sg.Button('0 - Sair')]
        ]

        window = sg.Window('Menu Grupo', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, '0 - Sair'):
                window.close()
                return 0
                
            if event.startswith('1'):
                window.close()
                return 1
            elif event.startswith('2'):
                window.close()
                return 2
            elif event.startswith('3'):
                window.close()
                return 3
            elif event.startswith('4'):
                window.close()
                return 4
            elif event.startswith('5'):
                window.close()
                return 5
            elif event.startswith('6'):
                window.close()
                return 6


    def pega_dados_grupo(self):
        layout = [
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('Descrição:'), sg.Input(key='descricao')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Cadastro de Grupo', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                dados = {
                    'nome': values['nome'],
                    'descricao': values['descricao']
                }
                window.close()
                return dados


    def seleciona_grupo(self):
        layout = [
            [sg.Text("Digite o ID do grupo:")],
            [sg.Input(key='id')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Grupo", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == "OK":
                try:
                    valor = int(values['id'])
                    window.close()
                    return valor
                except ValueError:
                    sg.popup("ID inválido! Digite um número inteiro.")


    def pega_cpf_pessoa(self):
        layout = [
            [sg.Text("Digite o CPF da pessoa:")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pessoa", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "OK":
                cpf = values['cpf'].strip()
                window.close()
                return cpf


    def lista_grupos(self, grupos):
        texto = "ID   | Nome | Membros | Descrição\n"
        texto += "="*75 + "\n"

        for g in grupos:
            texto += (
                f"{g['id']:<5} {g['nome']:<25} "
                f"{g['total_membros']:<10} {g['descricao']:<30}\n"
            )

        layout = [
            [sg.Multiline(texto, size=(80, 20), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Grupos Cadastrados", layout)
        window.read()
        window.close()


    def lista_membros(self, nome_grupo, membros):
        texto = f"MEMBROS DO GRUPO: {nome_grupo}\n" + "="*80 + "\n"
        texto += f"{'Nome':<30} {'CPF':<20} {'Telefone':<15}\n"
        texto += "-"*80 + "\n"

        for m in membros:
            texto += (
                f"{m['nome']:<30} {m['cpf']:<20} {m['telefone']:<15}\n"
            )

        layout = [
            [sg.Multiline(texto, size=(90, 25), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Membros", layout)
        window.read()
        window.close()


    def confirma_exclusao(self, nome_grupo):
        layout = [
            [sg.Text(f"Confirma a exclusão do grupo '{nome_grupo}'?")],
            [sg.Text("Todos os membros serão removidos do grupo.")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Exclusão", layout)

        event, values = window.read()
        window.close()

        return event == "Sim"


    def mostra_mensagem(self, msg: str):
        sg.popup(msg)
