from datetime import datetime
from view.tela_relatorio import TelaRelatorio
from collections import Counter

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
    
    def inicia(self):
        opcoes = {
            1: self.relatorio_financeiro_pacotes,
            2: self.gerar_relatorio,
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
        #sim!!! vc pensa em tudo mesmo
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
    
    def gerar_relatorio(self):
        """Gera e exibe o relatório completo do sistema"""
        
        destino_mais_popular = self.__calcular_destino_popular()
        destino_mais_caro = self.__calcular_destino_caro()
        destino_mais_barato = self.__calcular_destino_barato()
        
        # PASSEIOS
        passeio_mais_popular = self.__calcular_passeio_popular()
        passeio_mais_caro = self.__calcular_passeio_caro()
        passeio_mais_barato = self.__calcular_passeio_barato()
        
        dados = [
            destino_mais_popular, destino_mais_caro, destino_mais_barato,
            passeio_mais_popular, passeio_mais_caro, passeio_mais_barato
        ]
        
        self.__tela_relatorio.mostra_relatorio(dados)
    
    # ============= FUNÇÕES PRA CALCULAR E GERAR RELATÓRIO ============= #

    def __calcular_destino_popular (self):
        locais = self.__controlador_sistema.controlador_local_viagem.obter_locais()
        
        if not locais:
            return {'nome': "Nenhum destino cadastrado", 'visitas': 0}
        
        passeios = self.__controlador_sistema.controlador_passeio.obter_passeios()
        contagem_passeios = (
            f"{passeio.localizacao.cidade}, {passeio.localizacao.pais}" 
            for passeio in passeios
        )

        passagens = self.__controlador_sistema.controlador_passagem.obter_todas_passagens()
        contagem_passagens = (
            f"{passagem.local_destino.cidade}, {passagem.local_destino.pais}" 
            for passagem in passagens
        )

        contagem = Counter(contagem_passeios) + Counter(contagem_passagens)
        
        if not contagem:
            return {'nome': "Nenhum destino cadastrado", 'visitas': 0}

        nome, visitas = contagem.most_common(1)[0]
        # (1) retorna lista com item mais frequente e [0] a tupla ('cidade, país', numero)
        return {"nome": nome, "visitas": visitas}
    
    def __calcular_destino_caro(self):
        passagens = self.__controlador_sistema.controlador_passagem.obter_todas_passagens()
        
        if not passagens:
            return {'nome': "Nenhuma passagem cadastrada", 'valor': 0}
        
        passagem_mais_cara = passagens[0] #começando com a primeira
        
        for p in passagens:
            if p.valor > passagem_mais_cara.valor:
                passagem_mais_cara = p
        
        return {
            'nome': f"{passagem_mais_cara.local_destino.cidade}, {passagem_mais_cara.local_destino.pais}",
            'valor': passagem_mais_cara.valor
        }
        
    def __calcular_destino_barato(self):
        passagens = self.__controlador_sistema.controlador_passagem.obter_todas_passagens()
        
        if not passagens:
            return {'nome': "Nenhuma passagem cadastrada", 'valor': 0}
        
        passagem_mais_barata = passagens[0] #começando com a primeira
        
        for p in passagens:
            if p.valor < passagem_mais_barata.valor:
                passagem_mais_barata = p
        
        return {
            'nome': f"{passagem_mais_barata.local_destino.cidade}, {passagem_mais_barata.local_destino.pais}",
            'valor': passagem_mais_barata.valor
        }
    
    def __calcular_passeio_popular(self):
        passeios = self.__controlador_sistema.controlador_passeio.obter_passeios()
        
        if not passeios:
            return {"nome": "Nenhum passeio cadastrado", "quantidade": 0}
        
        pacotes = self.__controlador_sistema.controlador_pacote.obter_pacotes()
        
        atracoes = []
        for pacote in pacotes:
            for passeio in pacote.passeios:
                atracoes.append(passeio.atracao_turistica)
                
        if not atracoes:
            return {"nome": "Nenhuma passeio em pacotes", "quantidade": 0}
        
        contagem = Counter(atracoes)
        nome, quantidade = contagem.most_common(1)[0]
        
        return {'nome': nome, 'quantidade': quantidade}
    
    def __calcular_passeio_caro(self):
        passeios = self.__controlador_sistema.controlador_passeio.obter_passeios()
        
        if not passeios:
            return {'nome': "Nenhum passeio cadastrado", 'valor': 0}
        
        passeio_mais_caro = passeios[0] #começando com o primeiro
        
        for p in passeios:
            if p.valor > passeio_mais_caro.valor:
                passeio_mais_caro = p
        
        return {
            'nome': passeio_mais_caro.atracao_turistica,
            'valor': passeio_mais_caro.valor
        }
        
    def __calcular_passeio_barato(self):
        passeios = self.__controlador_sistema.controlador_passeio.obter_passeios()
        
        if not passeios:
            return {'nome': "Nenhum passeio cadastrado", 'valor': 0}
        
        passeio_mais_barato = passeios[0] #começando com o primeiro
        
        for p in passeios:
            if p.valor < passeio_mais_barato.valor:
                passeio_mais_barato = p
        
        return {
            'nome': passeio_mais_barato.atracao_turistica,
            'valor': passeio_mais_barato.valor
        }
