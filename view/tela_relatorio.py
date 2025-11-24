import FreeSimpleGUI as sg
from datetime import datetime

class TelaRelatorio:
    def __init__(self):
        pass

    def mostra_opcoes(self):
        layout = [
            [sg.Text("RELATÓRIOS", font=("Arial", 16), justification="center")],
            [sg.Button("1 - Relatório Financeiro (Pacotes)")],
            [sg.Button("2 - Relatório de Viagens")],
            [sg.Button("0 - Voltar")]
        ]

        window = sg.Window("Menu Relatórios", layout, modal=True)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "0 - Voltar"):
                window.close()
                return 0
            try:
                escolha = int(event[0])
                window.close()
                return escolha
            except Exception:
                sg.popup("Opção inválida")
                continue

    def mostra_relatorio_financeiro(self, dados: dict):
        """aqui ele vai mostrar todas as informações de pacotes e blablabla"""
        resumo = (
            f"Total de pacotes: {dados.get('total_pacotes',0)}\n"
            f"Receita esperada: R$ {dados.get('receita_esperada',0):.2f}\n"
            f"Receita recebida: R$ {dados.get('receita_recebida',0):.2f}\n"
            f"Receita pendente: R$ {dados.get('receita_pendente',0):.2f}\n"
            f"Percentual recebido: {dados.get('percentual_recebido',0):.2f}%\n\n"
            f"Pacotes totalmente pagos: {dados.get('pacotes_pagos',0)}\n"
            f"Pacotes parcialmente pagos: {dados.get('pacotes_parciais',0)}\n"
            f"Pacotes não pagos: {dados.get('pacotes_nao_pagos',0)}\n"
        )

        detalhes = "ID | Grupo | Valor Total | Valor Pago | Valor Restante | Status\n"
        detalhes += "-"*80 + "\n"
        for p in dados.get('detalhes_pacotes', []):
            detalhes += (
                f"{p.get('id')} | {p.get('grupo')[:18]:18} | "
                f"R$ {p.get('valor_total',0):8.2f} | R$ {p.get('valor_pago',0):8.2f} | "
                f"R$ {p.get('valor_restante',0):8.2f} | {p.get('status')}\n"
            )

        layout = [
            [sg.Text("RELATÓRIO FINANCEIRO", font=("Arial", 14, "bold"))],
            [sg.Text("Resumo:", font=("Arial", 11, "bold"))],
            [sg.Multiline(resumo, size=(80, 8), disabled=True)],
            [sg.Text("Detalhes por pacote:", font=("Arial", 11, "bold"))],
            [sg.Multiline(detalhes, size=(100, 20), disabled=True)],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Relatório Financeiro", layout, modal=True)
        window.read()
        window.close()
    
    def mostra_relatorio(self, dados):
        destino_popular, destino_caro, destino_barato, passeio_popular, passeio_caro, passeio_barato = dados
        
        layout = [
            [sg.Text('RELATÓRIO DO SISTEMA', font=("Arial", 14, "bold"), justification='center')],
            [sg.HorizontalSeparator()],
            
            [sg.Text('DESTINOS', font=("Arial", 12, "bold"))],
            [sg.Text(f"Mais Popular: {destino_popular['nome']} ({destino_popular['visitas']} visitas)")],
            [sg.Text(f"Mais Caro: {destino_caro['nome']} (R$ {destino_caro['valor']:.2f})")],
            [sg.Text(f"Mais Barato: {destino_barato['nome']} (R$ {destino_barato['valor']:.2f})")],
            
            [sg.HorizontalSeparator()],
            
            [sg.Text('PASSEIOS', font=("Arial", 12, "bold"))],
            [sg.Text(f"Mais Popular: {passeio_popular['nome']} ({passeio_popular['quantidade']} pacotes)")],
            [sg.Text(f"Mais Caro: {passeio_caro['nome']} (R$ {passeio_caro['valor']:.2f})")],
            [sg.Text(f"Mais Barato: {passeio_barato['nome']} (R$ {passeio_barato['valor']:.2f})")],
            
            [sg.HorizontalSeparator()],
            [sg.Button('Fechar')]
        ]
        
        window = sg.Window('Relatório', layout, modal=True)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                window.close()
                break

    def mostra_mensagem(self, msg: str):
        sg.popup(msg)