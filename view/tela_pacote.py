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

    #PEDIR ID DO GRUPO
    def pega_id_grupo(self):
        layout = [
            [sg.Text("Digite o ID do grupo:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Grupo", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or values["id"] == "":
            return -1
        
        try:
            return int(values["id"])
        except:
            return -1

    #PEDIR ÍNDICE
    def pega_indice(self):
        layout = [
            [sg.Text("Digite o número:")],
            [sg.Input(key="indice")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Índice", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or values["indice"] == "":
            return -1
        
        try:
            return int(values["indice"])
        except:
            return -1

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

        if event == "Cancelar" or values["numero"] == "":
            return -1
        
        try:
            return int(values["numero"])
        except:
            return -1

    #LISTAR PACOTES
    def lista_pacotes(self, pacotes):
        texto = "Nº | Grupo | Passagens | Passeios | Total | Pago | Restante\n"
        texto += "-"*90 + "\n"

        for p in pacotes:
            texto += f"{p['indice']} | {p['grupo'][:18]} | {p['total_passagens']} | {p['total_passeios']} | R$ {p['valor_total']:.2f} | R$ {p['valor_pago']:.2f} | R$ {p['valor_restante']:.2f}\n"

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
