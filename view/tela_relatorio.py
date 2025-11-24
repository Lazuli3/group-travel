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
        """Exibe o relatório financeiro com layout melhorado"""
        
        detalhes_tabela = []
        for p in dados.get('detalhes_pacotes', []):
            detalhes_tabela.append([
                p.get('id'),
                p.get('grupo', '')[:20],
                f"R$ {p.get('valor_total', 0):.2f}",
                f"R$ {p.get('valor_pago', 0):.2f}",
                f"R$ {p.get('valor_restante', 0):.2f}",
                p.get('status', '')
            ])
        
        layout = [
            [sg.Text("Relatório Financeiro", font=("Arial", 14, "bold"), justification='center', expand_x=True)],
            
            [sg.Frame('Resumo Geral', [
                [sg.Text(f"Total de pacotes:", size=(25, 1)), 
                sg.Text(f"{dados.get('total_pacotes', 0)}")],
                [sg.Text(f"Receita esperada:", size=(25, 1)), 
                sg.Text(f"R$ {dados.get('receita_esperada', 0):.2f}")],
                [sg.Text(f"Receita recebida:", size=(25, 1)), 
                sg.Text(f"R$ {dados.get('receita_recebida', 0):.2f}")],
                [sg.Text(f"Receita pendente:", size=(25, 1)), 
                sg.Text(f"R$ {dados.get('receita_pendente', 0):.2f}")],
                [sg.Text(f"Percentual recebido:", size=(25, 1)), 
                sg.Text(f"{dados.get('percentual_recebido', 0):.2f}%")],
                [sg.HorizontalSeparator()],
                [sg.Text(f"Pacotes totalmente pagos:", size=(25, 1)), 
                sg.Text(f"{dados.get('pacotes_pagos', 0)}")],
                [sg.Text(f"Pacotes parcialmente pagos:", size=(25, 1)), 
                sg.Text(f"{dados.get('pacotes_parciais', 0)}")],
                [sg.Text(f"Pacotes não pagos:", size=(25, 1)), 
                sg.Text(f"{dados.get('pacotes_nao_pagos', 0)}")],
            ], font=("Arial", 10), expand_x=True)],
            
            [sg.Table(
                values=detalhes_tabela,
                headings=['ID', 'Grupo', 'Valor Total', 'Valor Pago', 'Valor Restante', 'Status'],
                auto_size_columns=True,
                #col_widths=[5, 20, 12, 12, 14, 15],
                justification='left',
                num_rows=min(10, len(detalhes_tabela)) if detalhes_tabela else 1,
                key='-TABELA-',
                enable_events=False,
                display_row_numbers=False,
                alternating_row_color='#E8E8E8',
                header_background_color='#425261',
                header_text_color='white',
                background_color='white',
                text_color='black',
                expand_x=True
            )],
            
            [sg.Button("OK", size=(10, 1))]
        ]
        
        window = sg.Window("Relatório Financeiro", layout, size=(1000, 450), element_justification='center')
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'OK'):
                break
        
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