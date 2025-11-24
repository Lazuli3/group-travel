from controladores.controlador_pacote import ControladorPacote
from controladores.controlador_pagamento import ControladorPagamento
from controladores.controlador_passeio import ControladorPasseioTuristico
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_grupo import ControladorGrupo
from controladores.controlador_passagem import ControladorPassagem
from controladores.controlador_local_viagem import ControladorLocalViagem

from view.tela_sistema import TelaSistema

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_grupo = ControladorGrupo(self)
        self.__controlador_local_viagem = ControladorLocalViagem()
        self.__controlador_passagem = ControladorPassagem(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_passeio = ControladorPasseioTuristico(self)
        self.__controlador_pacote = ControladorPacote(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_relatorio = ControladorRelatorio(self)
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_grupo(self):
        return self.__controlador_grupo
    
    @property
    def controlador_local_viagem(self):
        return self.__controlador_local_viagem
    
    @property
    def controlador_passagem(self):
        return self.__controlador_passagem
    
    @property 
    def controlador_pacote(self):
        return self.__controlador_pacote
    
    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento
    
    @property
    def controlador_passeio(self):
        return self.__controlador_passeio
    
    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        self.abre_tela()

    def pessoa(self):
        self.__controlador_pessoa.inicia()

    def grupo(self):
        self.__controlador_grupo.inicia()

    def local_viagem(self):
        self.__controlador_local_viagem.inicia()

    def passagem(self):
        self.__controlador_passagem.inicia()

    def pacote(self):
        self.__controlador_pacote.inicia()

    def passeio(self):
        self.__controlador_passeio.inicia()

    def relatorio(self):
        self.__controlador_relatorio.inicia()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.pessoa, 2: self.grupo, 3:self.local_viagem, 4:self.passeio, 5:self.passagem, 6:self.pacote, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


    #============FUNÇÕES DO RELATÓRIO============
    
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
        
        self.__tela_sistema.mostrar_relatorio(dados)
    
    def __calcular_destino_popular (self):
        locais = self.__controlador_local_viagem.obter_locais()
        
        if not locais:
            return {'nome': "Nenhum destino cadastrado", 'visitas': 0}
        
        passeios = self.__controlador_passeio.obter_passeios()
        contagem_passeios = (
            f"{passeio.localizacao.cidade}, {passeio.localizacao.pais}" 
            for passeio in passeios
        )

        passagens = self.__controlador_passagem.obter_todas_passagens()
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
        passagens = self.__controlador_passagem.obter_todas_passagens()
        
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
        passagens = self.__controlador_passagem.obter_todas_passagens()
        
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
        passeios = self.__controlador_passeio.obter_passeios()
        
        if not passeios:
            return {"nome": "Nenhum passeio cadastrado", "quantidade": 0}
        
        pacotes = self.__controlador_pacote.obter_pacotes()
        
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
        passeios = self.__controlador_passeio.obter_passeios()
        
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
        passeios = self.__controlador_passeio.obter_passeios()
        
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
