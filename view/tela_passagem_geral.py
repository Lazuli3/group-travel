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
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Transporte", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values['id'] != '':
            try:
                return int(values["id"])
            except ValueError:
                sg.popup("Número inválido!")
                return None
        return None


    def lista_transportes(self, transportes):
        texto = f"{'Nº':<5} {'Tipo':<20} {'Empresa':<30} {'CNPJ':<20}\n"
        texto += "-" * 85 + "\n"

        for t in transportes:
            texto += f"{t.id:<5} {t.tipo:<20} {t.empresa.nome:<30} {t.empresa.cnpj:<20}\n"

        layout = [
            [sg.Multiline(texto, size=(90, 25), disabled=True)],
            [sg.Button("OK")]
        ]

        window = sg.Window("Transportes Cadastrados", layout)
        window.read()
        window.close()

#PASSAGENS

    def pega_dados_passagem(self, locais_disponiveis, transportes_disponiveis):

        # Verificação inicial
        if len(locais_disponiveis) < 2:
            sg.popup("É necessário ter pelo menos 2 locais cadastrados!")
            return None
        
        if not transportes_disponiveis:
            sg.popup("É necessário ter pelo menos 1 transporte cadastrado!")
            return None

        # Prepara lista amigável para exibir no Combo
        lista_locais = [
            f"{loc.id} - {loc.cidade}/{loc.pais}" for  loc in locais_disponiveis
        ]

        lista_transportes = [
            f"{t.id} - {t.tipo} ({t.empresa.nome})" for t in transportes_disponiveis
        ]

        layout = [
            [sg.Text("Transporte:"), sg.Combo(lista_transportes, key="transporte")],
            [sg.Text("Local de Origem:"), sg.Combo(lista_locais, key="origem")],
            [sg.Text("Local de Destino:"), sg.Combo(lista_locais, key="destino")],
            [sg.Text("Data da viagem (dd/mm/aaaa):"), sg.Input(key="data")],
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

                    if not values["transporte"]:
                        sg.popup("Selecione um transporte!")
                        continue
                
                    if not values["origem"]:
                        sg.popup("Selecione o local de origem!")
                        continue
                
                    if not values["destino"]:
                        sg.popup("Selecione o local de destino!")
                        continue
                    
                    #extrai o id do transporte
                    id_transporte = int(values["transporte"].split(" - ")[0])

                    #busca o transporte pelo id
                    transporte = None
                    for t in transportes_disponiveis:
                        if t.id == id_transporte:
                            transporte = t
                            break
                
                    if not transporte:
                        sg.popup("Transporte não encontrado!")
                        continue

                    # Extrai índices dos combos
                    id_origem = int(values["origem"].split(" - ")[0])
                    id_destino = int(values["destino"].split(" - ")[0])

                    if id_origem == id_destino:
                        sg.popup("Origem e destino não podem ser iguais!")
                        continue

                    local_origem = None
                    local_destino = None
                
                    for loc in locais_disponiveis:
                        if loc.id == id_origem:
                            local_origem = loc
                        if loc.id == id_destino:
                            local_destino = loc
                
                    if not local_origem or not local_destino:
                        sg.popup("Local não encontrado!")
                        continue

                    # Converte data
                    data = datetime.strptime(values["data"], "%d/%m/%Y")

                    # Converte valor (aceita vírgula ou ponto)
                    valor = float(values["valor"].replace(",", "."))

                    window.close()
                    return {
                        "transporte": transporte,  # Agora retorna o objeto
                        "local_origem": local_origem,
                        "local_destino": local_destino,
                        "data": data,
                        "valor": valor
                    }

                except ValueError as e:
                    sg.popup(f"Erro: Entrada inválida.\n{e}")
                except Exception as e:
                    sg.popup(f"Erro inesperado:\n{e}")



    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o número da passagem:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values['id'] != '':
            try:
                return int(values["id"])
            except ValueError:
                sg.popup("Número inválido!")
                return None
        return None


    def lista_passagens(self, passagens):
        texto = (
            f"{'Nº':<5} {'Data':<12} {'Origem':<25} {'Destino':<25} "
            f"{'Transporte':<20} {'Valor':<10}\n"
        )
        texto += "-" * 110 + "\n"

        for p in passagens:
            texto += (
                f"{p.id} "
                f"{p.data.strftime('%d/%m/%Y'):<12} "
                f"{p.local_origem.cidade}/{p.local_origem.pais:<25} "
                f"{p.local_destino.cidade}/{p.local_destino.pais:<25} "
                f"{p.transporte.tipo:<20} "
                f"R$ {p.valor:<10}\n"
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

    #métodos para integração com outras telas, uso para integração das exclusões

    def confirma_remocao_com_vinculo(self, mensagem):
        """
        Pergunta ao usuário como proceder quando há vínculos
        Retorna: 'remover', 'cancelar'
        """
        layout = [
            [sg.Text("⚠️ ATENÇÃO", font=("Arial", 14, "bold"))],
            [sg.Text(mensagem)],
            [sg.Text("\nO que deseja fazer?")],
            [sg.Button("Remover dos Pacotes e Excluir"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Confirmação de Exclusão", layout)
        event, _ = window.read()
        window.close()

        if event == "Remover dos Pacotes e Excluir":
            return "remover"
        return "cancelar"
