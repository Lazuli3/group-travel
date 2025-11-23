import FreeSimpleGUI as sg

class TelaPacote:
    """Interface gráfica de pacotes usando FreeSimpleGUI"""

    # ===================== MENU PRINCIPAL ======================
    def mostra_opcoes(self):
        layout = [
            [sg.Text("GERENCIAMENTO DE PACOTES", justification='center', font=("Arial", 16))],
            [sg.Button("1 - Incluir Pacote")],
            [sg.Button("2 - Listar Pacotes")],
            [sg.Button("3 - Alterar Pacote")],
            [sg.Button("4 - Excluir Pacote")],
            [sg.Button("0 - Voltar")],
        ]

        window = sg.Window("Menu de Pacotes", layout)
        event, values = window.read()
        window.close()

        if event is None:
            return 0
        return int(event[0])  # pega apenas o primeiro caractere da string "1 - ...."

    def mostra_menu_alteracao(self):
        """Menu de opções para alteração"""
        layout = [
            [sg.Text("MENU DE ALTERAÇÃO", font=("Arial", 14))],
            [sg.Button("1 - Adicionar Passagem")],
            [sg.Button("2 - Remover Passagem")],
            [sg.Button("3 - Adicionar Passeio")],
            [sg.Button("4 - Remover Passeio")],
            [sg.Button("5 - Adicionar Pagamento")],
            [sg.Button("0 - Cancelar")]
        ]

        window = sg.Window("Alteração de Pacote", layout)
        event, values = window.read()
        window.close()

        if event is None or event == "0 - Cancelar":
            return 0
        
        return int(event[0])
    
    #PEDIR ID
    def pega_id_grupo(self):
        layout = [
            [sg.Text("Digite o ID do grupo:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Grupo", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return False
        return False

    def pega_id_passeio(self):
        """Pede o ID do passeio"""
        layout = [
            [sg.Text("Digite o ID do passeio:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Passeio", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return False
        return False

    def pega_id_passagem(self):
        """Pede o ID da passagem"""
        layout = [
            [sg.Text("Digite o ID da passagem:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID da Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return False
        return False

    #CONFIRMA ADIÇÃO
    def confirma_adicao(self, tipo):
        layout = [
            [sg.Text(f"Deseja adicionar {tipo}?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Adição", layout)
        event, values = window.read()
        window.close()

        return event == "Sim"

    #SELECIONA PACOTE
    def seleciona_pacote(self):
        layout = [
            [sg.Text("Digite o número do pacote:")],
            [sg.Input(key="numero")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pacote", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return False
        return False


    def seleciona_membro(self, membros):
        """Mostra lista de membros e retorna o ID escolhido"""
        texto = "--- MEMBROS DO GRUPO ---\n\n"
        
        for membro in membros:
            texto += f"ID {membro.id}: {membro.nome} (CPF: {membro.cpf})\n"
        
        layout = [
            [sg.Multiline(texto, size=(50, 10), disabled=True)],
            [sg.Text("Digite o ID do membro:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Membro", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return False
        return False

    #LISTAR PACOTES
    def lista_pacotes(self, pacotes):
        texto = "Nº | Grupo | Passagens | Passeios | Total | Pago | Restante\n"
        texto += "-"*90 + "\n"

        for p in pacotes:
            texto += f"{p['id']} | {p['grupo'][:18]} | {p['total_passagens']} | {p['total_passeios']} | R$ {p['valor_total']:.2f} | R$ {p['valor_pago']:.2f} | R$ {p['valor_restante']:.2f}\n"

        layout = [
            [sg.Multiline(texto, size=(90, 20), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Lista de Pacotes", layout)
        window.read()
        window.close()

    #CONFIRMA EXCLUSÃO
    def confirma_exclusao(self, nome_grupo):
        layout = [
            [sg.Text(f"Deseja excluir o pacote do grupo '{nome_grupo}'?")],
            [sg.Button("Sim"), sg.Button("Não")],
        ]

        window = sg.Window("Excluir Pacote", layout)
        event, _ = window.read()
        window.close()

        return event == "Sim"

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)
