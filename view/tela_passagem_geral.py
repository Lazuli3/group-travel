import FreeSimpleGUI as sg
from datetime import datetime

class TelaPassagemGeral:

    # MENU PRINCIPAL
    def mostra_opcoes(self):
        layout = [
            [sg.Text("GERENCIAMENTO DE VIAGENS", font=("Arial", 14, "bold"), justification="center")],
            [sg.Text("EMPRESAS:", font=("Arial", 12, "bold"))],
            [sg.Button("1 - Cadastrar Empresa")],
            [sg.Button("2 - Listar Empresas")],
            [sg.Button("3 - Excluir Empresa")],
            [sg.Text("")],
            [sg.Text("TRANSPORTES:", font=("Arial", 12, "bold"))],
            [sg.Button("4 - Cadastrar Transporte")],
            [sg.Button("5 - Listar Transportes")],
            [sg.Button("6 - Excluir Transporte")],
            [sg.Text("")],
            [sg.Text("PASSAGENS:", font=("Arial", 12, "bold"))],
            [sg.Button("7 - Cadastrar Passagem")],
            [sg.Button("8 - Listar Passagens")],
            [sg.Button("9 - Excluir Passagem")],
            [sg.Text("")],
            [sg.Button("0 - Voltar")]
        ]

        window = sg.Window("Menu Passagens", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "0 - Voltar"):
                window.close()
                return 0

            for i in range(1, 10):
                if event.startswith(str(i)):
                    window.close()
                    return i

    # EMPRESAS
    def pega_dados_empresa(self):
        layout = [
            [sg.Text("Nome da empresa:"), sg.Input(key="nome")],
            [sg.Text("CNPJ:"), sg.Input(key="cnpj")],
            [sg.Text("Telefone:"), sg.Input(key="telefone")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Empresa", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Confirmar":
                window.close()
                return values


    def pega_cnpj(self):
        layout = [
            [sg.Text("Digite o CNPJ da empresa:")],
            [sg.Input(key="cnpj")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Excluir Empresa", layout)
        event, values = window.read()
        window.close()

        if event == "OK":
            return values["cnpj"]
        return None


    def lista_empresas(self, empresas):
        texto = f"{'Nome':<30} {'CNPJ':<20} {'Telefone':<15}\n"
        texto += "-" * 70 + "\n"

        for emp in empresas:
            texto += f"{emp.nome:<30} {emp.cnpj:<20} {emp.telefone:<15}\n"

        layout = [
            [sg.Multiline(texto, size=(80, 20), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Empresas Cadastradas", layout)
        window.read()
        window.close()

    # TRANSPORTES
    def pega_dados_transporte(self):
        layout = [
            [sg.Text("Tipo de transporte (Ônibus / Avião / Van / etc):")],
            [sg.Input(key="tipo")],
            [sg.Text("CNPJ da empresa:")],
            [sg.Input(key="cnpj_empresa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Transporte", layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Confirmar":
                window.close()
                return values


    def seleciona_transporte(self):
        layout = [
            [sg.Text("Digite o número do transporte:")],
            [sg.Input(key="indice")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Transporte", layout)
        event, values = window.read()
        window.close()

        if event == "OK":
            try:
                return int(values["indice"])
            except ValueError:
                sg.popup("Número inválido!")
                return -1
        return -1


    def lista_transportes(self, transportes):
        texto = f"{'Nº':<5} {'Tipo':<20} {'Empresa':<30} {'CNPJ':<20}\n"
        texto += "-" * 85 + "\n"

        for i, t in enumerate(transportes):
            texto += f"{i:<5} {t.tipo:<20} {t.empresa.nome:<30} {t.empresa.cnpj:<20}\n"

        layout = [
            [sg.Multiline(texto, size=(90, 25), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Transportes Cadastrados", layout)
        window.read()
        window.close()

    # PASSAGENS
    def pega_dados_passagem(self, controlador_local_viagem):
        locais = controlador_local_viagem._ControladorLocalViagem__locais_viagem

        if len(locais) < 2:
            sg.popup("É necessário ter pelo menos 2 locais cadastrados!")
            return None

        lista_locais = [
            f"{i} - {loc.cidade}/{loc.pais}" for i, loc in enumerate(locais)
        ]

        layout = [
            [sg.Text("Número do transporte:"), sg.Input(key="indice_transporte")],
            [sg.Text("Origem:"), sg.Combo(lista_locais, key="origem")],
            [sg.Text("Destino:"), sg.Combo(lista_locais, key="destino")],
            [sg.Text("Data (dd/mm/aaaa):"), sg.Input(key="data")],
            [sg.Text("Valor (R$):"), sg.Input(key="valor")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Passagem", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Confirmar":

                try:
                    indice_transporte = int(values["indice_transporte"])
                    indice_origem = int(values["origem"].split(" - ")[0])
                    indice_destino = int(values["destino"].split(" - ")[0])

                    if indice_origem == indice_destino:
                        sg.popup("Origem e destino não podem ser iguais!")
                        continue

                    data = datetime.strptime(values["data"], "%d/%m/%Y")
                    valor = float(values["valor"].replace(",", "."))

                    window.close()
                    return {
                        "indice_transporte": indice_transporte,
                        "local_origem": locais[indice_origem],
                        "local_destino": locais[indice_destino],
                        "data": data,
                        "valor": valor
                    }

                except Exception as e:
                    sg.popup(f"Erro: {e}")


    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o número da passagem:")],
            [sg.Input(key="indice")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "OK":
            try:
                return int(values["indice"])
            except ValueError:
                sg.popup("Número inválido!")
                return -1
        return -1


    def lista_passagens(self, passagens):
        texto = (
            f"{'Nº':<5} {'Data':<12} {'Origem':<25} {'Destino':<25} "
            f"{'Transporte':<20} {'Valor':<10}\n"
        )
        texto += "-" * 110 + "\n"

        for i, p in enumerate(passagens):
            texto += (
                f"{i:<5} "
                f"{p.data.strftime('%d/%m/%Y'):<12} "
                f"{p.local_origem.cidade}/{p.local_origem.pais:<25} "
                f"{p.local_destino.cidade}/{p.local_destino.pais:<25} "
                f"{p.transporte.tipo:<20} "
                f"R$ {p.valor:.2f:<10}\n"
            )

        layout = [
            [sg.Multiline(texto, size=(110, 25), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Passagens Cadastradas", layout)
        window.read()
        window.close()

    def mostra_mensagem(self, msg: str):
        sg.popup(msg)
