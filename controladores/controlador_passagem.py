from entidades.empresa import Empresa
from entidades.transporte import Transporte
from entidades.passagem import Passagem
from view.tela_passagem_geral import TelaPassagemGeral
from datetime import datetime

from DAOs.empresa_dao import EmpresaDAO
from DAOs.transporte_dao import TransporteDAO
from DAOs.passagem_dao import PassagemDAO

class ControladorPassagem:

    def __init__(self, controlador_sistema, controlador_local_viagem):
        self.__empresa_dao = EmpresaDAO()
        self.__transporte_dao = TransporteDAO()
        self.__passagem_dao = PassagemDAO()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_local = controlador_local_viagem
        self.__tela_passagem = TelaPassagemGeral()
        
        self.__proximo_id_transporte = self.__gerar_proximo_id_transporte()
        self.__proximo_id_passagem = self.__gerar_proximo_id_passagem()
    
    def __gerar_proximo_id_transporte(self):
        transportes = list(self.__transporte_dao.get_all())
        if not transportes:
            return 1
        max_id = max(t.id for t in transportes)
        return max_id + 1
    
    def __gerar_proximo_id_passagem(self):
        passagens = list(self.__passagem_dao.get_all())
        if not passagens:
            return 1
        max_id = max(p.id for p in passagens)
        return max_id + 1
    
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
            opcao = self.__tela_passagem.mostra_opcoes()
            
            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_passagem.mostra_mensagem('Opção inválida.')
    
    #EMPRESAS
    
    def incluir_empresa(self):
        try:
            dados = self.__tela_passagem.pega_dados_empresa()
            
            if self.buscar_empresa_por_cnpj(dados['cnpj']):
                self.__tela_passagem.mostra_mensagem(f"Empresa com CNPJ {dados['cnpj']} já cadastrada!")
                return
            
            empresa = Empresa(**dados)
            self.__empresa_dao.add(empresa)
            print(empresa.cnpj)
            self.__tela_passagem.mostra_mensagem("Empresa cadastrada com sucesso.")

        
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao cadastrar empresa: {str(e)}")
    
    def listar_empresas(self):
        empresas = list(self.__empresa_dao.get_all())
        
        if not empresas:
            self.__tela_passagem.mostra_mensagem('Nenhuma empresa cadastrada')
        else:
            self.__tela_passagem.lista_empresas(empresas)
    
    def excluir_empresa(self):
        try:
            cnpj = self.__tela_passagem.pega_cnpj()
            empresa = self.buscar_empresa_por_cnpj(cnpj)
            
            if empresa:
                transportes = list(self.__transporte_dao.get_all())
                transportes_vinculados = [t for t in transportes if t.empresa.cnpj == cnpj]
                
                if transportes_vinculados:
                    self.__tela_passagem.mostra_mensagem(
                        f"Não é possível excluir! A empresa possui {len(transportes_vinculados)} transporte(s) vinculado(s)."
                    )
                    return
                
                self.__empresa_dao.remove(cnpj)
                self.__tela_passagem.mostra_mensagem(f"A empresa {empresa.nome} foi removida com sucesso.")
            else:
                self.__tela_passagem.mostra_mensagem("Essa empresa não está cadastrada no sistema.")
        
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao excluir empresa: {str(e)}")
    
    def buscar_empresa_por_cnpj(self, cnpj):
        return self.__empresa_dao.get(cnpj)
    
    #TRANSPORTES
    
    def incluir_transporte(self):
        empresas = list(self.__empresa_dao.get_all())
        
        if not empresas:
            self.__tela_passagem.mostra_mensagem("Nenhuma empresa cadastrada. Cadastre uma empresa primeiro!")
            return
        
        try:
            self.listar_empresas()
            
            dados = self.__tela_passagem.pega_dados_transporte()
            
            empresa = self.buscar_empresa_por_cnpj(dados['cnpj_empresa'])
            if not empresa:
                self.__tela_passagem.mostra_mensagem(f"Empresa com CNPJ {dados['cnpj_empresa']} não encontrada!")
                return
            
            #criando um id dentro do próprio controlador
            transporte = Transporte(dados['tipo'], empresa, self.__proximo_id_transporte)
            
            self.__transporte_dao.add(transporte)
            self.__proximo_id_transporte += 1
            
            self.__tela_passagem.mostra_mensagem("Transporte cadastrado com sucesso.")
        
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao cadastrar transporte: {str(e)}")
    
    def listar_transportes(self):
        transportes = list(self.__transporte_dao.get_all())
        
        if not transportes:
            self.__tela_passagem.mostra_mensagem('Nenhum transporte cadastrado.')
            return
        
        self.__tela_passagem.lista_transportes(transportes)
    
    def excluir_transporte(self):
        transportes = list(self.__transporte_dao.get_all())
        
        if not transportes:
            self.__tela_passagem.mostra_mensagem('Nenhum transporte cadastrado.')
            return
        
        try:
            self.listar_transportes()
            indice = self.__tela_passagem.seleciona_transporte()
            
            transportes_lista = list(transportes)
            if 0 <= indice < len(transportes_lista):
                transporte = transportes_lista[indice]
                
                passagens = list(self.__passagem_dao.get_all())
                passagens_vinculadas = [p for p in passagens if p.transporte.id == transporte.id]
                
                if passagens_vinculadas:
                    self.__tela_passagem.mostra_mensagem(
                        f"Não é possível excluir! O transporte possui {len(passagens_vinculadas)} passagem(ns) vinculada(s)."
                    )
                    return
                
                self.__transporte_dao.remove(transporte.id)
                self.__tela_passagem.mostra_mensagem(f"O transporte foi removido com sucesso.")
            else:
                self.__tela_passagem.mostra_mensagem("Índice inválido!")
        
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao excluir transporte: {str(e)}")
    
    #PASSAGENS
    
    def incluir_passagem(self):
        """Cadastra uma nova passagem"""
        transportes = list(self.__transporte_dao.get_all())
        
        if not transportes:
            self.__tela_passagem.mostra_mensagem(
                "Nenhum transporte cadastrado. Cadastre um transporte primeiro!"
            )
            return False
        
        # ✅ Controlador obtém os dados
        locais = self.__controlador_local.obter_locais()
        
        if not locais or len(locais) < 2:
            self.__tela_passagem.mostra_mensagem(
                "É necessário ter pelo menos 2 locais cadastrados!"
            )
            return False
        
        try:
            self.listar_transportes()

            # ✅ CORRETO: Passa apenas os DADOS para a View
            dados = self.__tela_passagem.pega_dados_passagem(locais)
            
            if dados is None:
                self.__tela_passagem.mostra_mensagem("Cadastro de passagem cancelado.")
                return False
            
            # Validações
            transportes_lista = list(transportes)
            if dados['indice_transporte'] < 0 or dados['indice_transporte'] >= len(transportes_lista):
                self.__tela_passagem.mostra_mensagem("Transporte inválido!")
                return False
            
            transporte = transportes_lista[dados['indice_transporte']]
            local_origem = dados['local_origem']
            local_destino = dados['local_destino']
            
            if local_origem == local_destino:
                self.__tela_passagem.mostra_mensagem("Origem e destino não podem ser iguais!")
                return False
            
            # Cria passagem
            passagem = Passagem(
                dados['data'],
                dados['valor'],
                local_origem,
                local_destino,
                transporte,
                self.__proximo_id_passagem
            )
            
            self.__passagem_dao.add(passagem)
            self.__proximo_id_passagem += 1
            
            self.__tela_passagem.mostra_mensagem("Passagem cadastrada com sucesso.")
            return True
        
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao cadastrar passagem: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

        
    def listar_passagens(self):
        """Lista todas as passagens cadastradas"""
        passagens = list(self.__passagem_dao.get_all())
            
        if not passagens:
            self.__tela_passagem.mostra_mensagem('Nenhuma passagem cadastrada.')
            return
            
        self.__tela_passagem.lista_passagens(passagens)
        
    def excluir_passagem(self):
        """Exclui uma passagem"""
        passagens = list(self.__passagem_dao.get_all())
            
        if not passagens:
            self.__tela_passagem.mostra_mensagem('Nenhuma passagem cadastrada.')
            return False
            
        try:
            self.listar_passagens()
            indice = self.__tela_passagem.seleciona_passagem()
                
            passagens_lista = list(passagens)
            if 0 <= indice < len(passagens_lista):
                passagem = passagens_lista[indice]
                self.__passagem_dao.remove(passagem.id)
                self.__tela_passagem.mostra_mensagem("Passagem removida com sucesso.")
                return True
            else:
                self.__tela_passagem.mostra_mensagem("Índice inválido!")
                return False
            
        except Exception as e:
            self.__tela_passagem.mostra_mensagem(f"Erro ao excluir passagem: {str(e)}")
            return False
        
        # ====== MÉTODOS PÚBLICOS ======
        
    def obter_todas_empresas(self):
        """Retorna lista de todas as empresas"""
        return list(self.__empresa_dao.get_all())
        
    def obter_todos_transportes(self):
        """Retorna lista de todos os transportes"""
        return list(self.__transporte_dao.get_all())
        
    def obter_todas_passagens(self):
        """Retorna lista de todas as passagens"""
        return list(self.__passagem_dao.get_all())
        
    def sair(self):
        """Sai do menu de passagens"""
        self.__tela_passagem.mostra_mensagem('Encerrando o gerenciamento de passagem.')
        return True