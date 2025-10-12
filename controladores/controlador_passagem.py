from entidades.empresa import Empresa
from entidades.transporte import Transporte
from entidades.passagem import Passagem
from view.tela_passagem_geral import TelaPassagemGeral
from datetime import datetime

class ControladorPassagem:

    def __init__(self, controlador_local_viagem):
        self.__empresas = []
        self.__transportes = []
        self.__passagens = []
        self.controlador_local_viagem = controlador_local_viagem 
        self.__tela_passagem_geral = TelaPassagemGeral()
    
    def inicia(self):
        opcoes = {
            1: self.incluir_empresa,
            2: self.listar_empresas,
            3: self.excluir_empresa,
            4: self.incluir_transporte,
            5: self.listar_transportes,
            6: self.excluir_transporte,
            7: self.incluir_passagem,
            8: self.listar_passagens,
            9: self.excluir_passagem,
            0: self.sair
        }
        
        while True:
            opcao = self.__tela_passagem_geral.mostra_opcoes()
            
            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_passagem_geral.mostra_mensagem('Opção inválida.')
    
    #EMPRESAS
    
    def incluir_empresa(self):
        try:
            dados = self.__tela_passagem_geral.pega_dados_empresa()
            
            if self.buscar_empresa_por_cnpj(dados['cnpj']):
                self.__tela_passagem_geral.mostra_mensagem(f"Empresa com CNPJ {dados['cnpj']} já cadastrada!")
                return
            
            empresa = Empresa(**dados)
            self.__empresas.append(empresa)
            self.__tela_passagem_geral.mostra_mensagem("Empresa cadastrada com sucesso.")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao cadastrar empresa: {str(e)}")
    
    def listar_empresas(self):
        if not self.__empresas:
            self.__tela_passagem_geral.mostra_mensagem('Nenhuma empresa cadastrada.')
            return
        
        self.__tela_passagem_geral.lista_empresas(self.__empresas)
    
    def excluir_empresa(self):
        try:
            cnpj = self.__tela_passagem_geral.pega_cnpj()
            empresa = self.buscar_empresa_por_cnpj(cnpj)
            
            if empresa:
                #vê se existe algum transporte vinculado á empresa
                transportes_vinculados = [t for t in self.__transportes if t.empresa == empresa]
                if transportes_vinculados:
                    self.__tela_passagem_geral.mostra_mensagem(
                        f"Não é possível excluir! A empresa possui {len(transportes_vinculados)} transporte(s) vinculado(s)."
                    )
                    return
                
                self.__empresas.remove(empresa)
                self.__tela_passagem_geral.mostra_mensagem(f"A empresa {empresa.nome} foi removida com sucesso.")
            else:
                self.__tela_passagem_geral.mostra_mensagem("Essa empresa não está cadastrada no sistema.")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao excluir empresa: {str(e)}")
    
    def buscar_empresa_por_cnpj(self, cnpj):
        for empresa in self.__empresas:
            if empresa.cnpj == cnpj:
                return empresa
        return None
    
    #TRANSPORTES
    
    def incluir_transporte(self):
        if not self.__empresas:
            self.__tela_passagem_geral.mostra_mensagem("Nenhuma empresa cadastrada. Cadastre uma empresa primeiro!")
            return
        
        try:
            self.listar_empresas()
            
            dados = self.__tela_passagem_geral.pega_dados_transporte()

            empresa = self.buscar_empresa_por_cnpj(dados['cnpj_empresa'])
            if not empresa:
                self.__tela_passagem_geral.mostra_mensagem(f"Empresa com CNPJ {dados['cnpj_empresa']} não encontrada!")
                return
            
            transporte = Transporte(dados['tipo'], empresa)
            self.__transportes.append(transporte)
            self.__tela_passagem_geral.mostra_mensagem("Transporte cadastrado com sucesso.")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao cadastrar transporte: {str(e)}")
    
    def listar_transportes(self):
        if not self.__transportes:
            self.__tela_passagem_geral.mostra_mensagem('Nenhum transporte cadastrado.')
            return
        
        self.__tela_passagem_geral.lista_transportes(self.__transportes)
    
    def excluir_transporte(self):
        if not self.__transportes:
            self.__tela_passagem_geral.mostra_mensagem('Nenhum transporte cadastrado.')
            return
        
        try:
            self.listar_transportes()
            indice = self.__tela_passagem_geral.seleciona_transporte()
            
            if 0 <= indice < len(self.__transportes):
                transporte = self.__transportes[indice]

                passagens_vinculadas = [p for p in self.__passagens if p.transporte == transporte]
                if passagens_vinculadas:
                    self.__tela_passagem_geral.mostra_mensagem(
                        f"Não é possível excluir! O transporte possui {len(passagens_vinculadas)} passagem(ns) vinculada(s)."
                    )
                    return
                
                self.__transportes.remove(transporte)
                self.__tela_passagem_geral.mostra_mensagem(f"O transporte {transporte} foi removido com sucesso.")
            else:
                self.__tela_passagem_geral.mostra_mensagem("Índice inválido!")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao excluir transporte: {str(e)}")
    
    #PASSAGENS
    
    def incluir_passagem(self):
        if not self.__transportes:
            self.__tela_passagem_geral.mostra_mensagem("Nenhum transporte cadastrado. Cadastre um transporte primeiro!")
            return
        
        #precisa ter pelo menos 2 locais de viagem cadastrados, o local de origem e o de destino não podem ser os mesmos
        if not self.controlador_local_viagem._ControladorLocalViagem__locais_viagem:
            self.__tela_passagem_geral.mostra_mensagem("Nenhum local de viagem cadastrado. Cadastre locais primeiro!")
            return
        
        try:
            self.listar_transportes()

            dados = self.__tela_passagem_geral.pega_dados_passagem(self.controlador_local_viagem)

            if dados is None:
                self.__tela_passagem_geral.mostra_mensagem("Cadastro de passagem cancelado.")
                return
            
            if dados['indice_transporte'] < 0 or dados['indice_transporte'] >= len(self.__transportes):
                self.__tela_passagem_geral.mostra_mensagem("Transporte inválido!")
                return
            
            transporte = self.__transportes[dados['indice_transporte']]
            
            local_origem = dados['local_origem']
            
            local_destino = dados['local_destino']
            
            if local_origem == local_destino:
                self.__tela_passagem_geral.mostra_mensagem("Origem e destino não podem ser iguais!")
                return
            
            #aqui ele cria a passagem
            passagem = Passagem(
                dados['data'],
                dados['valor'],
                local_origem,
                local_destino,
                transporte
            )
            
            self.__passagens.append(passagem)
            self.__tela_passagem_geral.mostra_mensagem("Passagem cadastrada com sucesso.")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao cadastrar passagem: {str(e)}")
    
    def listar_passagens(self):
        if not self.__passagens:
            self.__tela_passagem_geral.mostra_mensagem('Nenhuma passagem cadastrada.')
            return
        
        self.__tela_passagem_geral.lista_passagens(self.__passagens)
    
    def excluir_passagem(self):
        if not self.__passagens:
            self.__tela_passagem_geral.mostra_mensagem('Nenhuma passagem cadastrada.')
            return
        
        try:
            self.listar_passagens()
            indice = self.__tela_passagem_geral.seleciona_passagem()
            
            if 0 <= indice < len(self.__passagens):
                passagem = self.__passagens[indice]
                self.__passagens.remove(passagem)
                self.__tela_passagem_geral.mostra_mensagem("Passagem removida com sucesso.")
            else:
                self.__tela_passagem_geral.mostra_mensagem("Índice inválido!")
        
        except Exception as e:
            self.__tela_passagem_geral.mostra_mensagem(f"Erro ao excluir passagem: {str(e)}")
    
    def sair(self):
        self.__tela_passagem_geral.mostra_mensagem('Encerrando o gerenciamento de passagem.')
        return True