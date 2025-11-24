from datetime import datetime
from view.tela_relatorio import TelaRelatorio

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
    
    def inicia(self):
        opcoes = {
            1: self.relatorio_financeiro_pacotes,
            0: self.sair
        }
        
        while True:
            opcao = self.__tela_relatorio.mostra_opcoes()
            
            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_relatorio.mostra_mensagem('Opção inválida.')
    
    def relatorio_financeiro_pacotes(self):
        """relatório financeiro completo dos pacotes"""
        '''adicionei o método obter_pacotes no controlador_pacote para não furar o mvc'''
        pacotes = self.__controlador_sistema.controlador_pacote.obter_pacotes()
        
        if not pacotes:
            self.__tela_relatorio.mostra_mensagem("Nenhum pacote cadastrado.")
            return
        
        #variaveis vazias para coleta de dados
        total_receita_esperada = 0
        total_receita_recebida = 0
        total_receita_pendente = 0
        
        pacotes_pagos = []
        pacotes_parciais = []
        pacotes_nao_pagos = []
        
        for pacote in pacotes:
            valor_total = pacote.valor_total()
            valor_pago = pacote.calcular_valor_pago()
            valor_restante = pacote.calcular_valor_restante()
            
            total_receita_esperada += valor_total
            total_receita_recebida += valor_pago
            total_receita_pendente += valor_restante

            if valor_restante == 0:
                pacotes_pagos.append(pacote)
            elif valor_pago > 0:
                pacotes_parciais.append(pacote)
            else:
                pacotes_nao_pagos.append(pacote)
        
        #aqui ele abre os dados dos pacotes em um dicionario
        dados = {
            'total_pacotes': len(list(pacotes)),
            'receita_esperada': total_receita_esperada,
            'receita_recebida': total_receita_recebida,
            'receita_pendente': total_receita_pendente,
            'percentual_recebido': (total_receita_recebida / total_receita_esperada * 100) if total_receita_esperada > 0 else 0,
            'pacotes_pagos': len(pacotes_pagos),
            'pacotes_parciais': len(pacotes_parciais),
            'pacotes_nao_pagos': len(pacotes_nao_pagos),
            'detalhes_pacotes': []
        }
        
        #detalhando
        for pacote in pacotes:
            dados['detalhes_pacotes'].append({
                'id': pacote.id,
                'grupo': pacote.grupo.nome,
                'valor_total': pacote.valor_total(),
                'valor_pago': pacote.calcular_valor_pago(),
                'valor_restante': pacote.calcular_valor_restante(),
                'status': self._determinar_status_pagamento(pacote)
            })
        
        self.__tela_relatorio.mostra_relatorio_financeiro(dados)
    
    def _determinar_status_pagamento(self, pacote):
        '''legal para prestar atenção, consegui implementar pq essas funções JA existem em pacote, legal né?'''
        valor_restante = pacote.calcular_valor_restante()
        valor_pago = pacote.calcular_valor_pago()
        
        if valor_restante == 0:
            return "PAGO"
        elif valor_pago > 0:
            return "PARCIAL"
        else:
            return "NÃO PAGO"
    
    def sair(self):
        self.__tela_relatorio.mostra_mensagem('Encerrando relatórios.')
        return True