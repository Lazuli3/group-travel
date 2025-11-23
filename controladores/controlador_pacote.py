from entidades.pacote import Pacote
from view.tela_pacote import TelaPacote
from DAOs.pacote_dao import PacoteDAO

class ControladorPacote:
    
    def __init__(self, controlador_sistema):
        self.__pacotes_DAO = PacoteDAO()
        self.__tela_pacote = TelaPacote()
        self.__controlador_sistema = controlador_sistema
        self.__proximo_id = self.__gerar_proximo_id()

    def __gerar_proximo_id(self):
        """Gera o próximo ID disponível baseado nos locais existentes"""
        pacotes = list(self.__pacotes_DAO.get_all())
        if not pacotes:
            return 1
        
        max_id = max(pacote.id for pacote in pacotes)
        return max_id + 1
    
    def buscar_por_id(self, pacote_id):
        return self.__pacotes_DAO.get(pacote_id)
    
    def inicia(self):
        opcoes = {
            1: self.incluir_pacote,
            2: self.listar_pacotes,
            3: self.alterar_pacote,
            4: self.excluir_pacote,
            0: self.sair
        }
        
        while True:
            opcao = self.__tela_pacote.mostra_opcoes()
            
            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_pacote.mostra_mensagem('Opção inválida.')
    
    def incluir_pacote(self):
        try:
            # Verifica se há grupos cadastrados
            if not self.__controlador_sistema.controlador_grupo.obter_todos_grupos():
                self.__tela_pacote.mostra_mensagem("Nenhum grupo cadastrado. Cadastre um grupo primeiro!")
                return
            
            # Mostra grupos disponíveis
            print("\n--- GRUPOS DISPONÍVEIS ---")
            self.__controlador_sistema.controlador_grupo.listar_grupos()
            
            # Seleciona grupo
            id_grupo = self.__tela_pacote.pega_id_grupo()
            if not id_grupo:
                return

            grupo = self.__controlador_sistema.controlador_grupo.buscar_por_id(id_grupo)
            
            if not grupo:
                self.__tela_pacote.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return
            
            # Cria pacote vazio para o grupo
            pacote = Pacote(self.__proximo_id, [], [], grupo)
            
            # Adiciona passagens (opcional)
            if self.__controlador_sistema.controlador_passagem.obter_todas_passagens():
                print("\n--- ADICIONAR PASSAGENS ---")
                while True:
                    self.__controlador_sistema.controlador_passagem.listar_passagens()
                    adicionar = self.__tela_pacote.confirma_adicao("passagem")
                    if not adicionar:
                        break
                    
                    id_passagem = self.__tela_pacote.pega_id_passagem()
                    if not id_passagem:
                        continue
                    
                    passagem = self.__controlador_sistema.controlador_passagem.buscar_por_id(id_passagem)
                    
                    if passagem:
                        pacote.adicionar_passagem(passagem)
                        self.__tela_pacote.mostra_mensagem("Passagem adicionada!")

                    else:
                        self.__tela_pacote.mostra_mensagem("Passagem não encontrada!")
            
            # Adiciona passeios (opcional)
            if self.__controlador_sistema.controlador_passeio.obter_passeios():
                print("\n--- ADICIONAR PASSEIOS ---")
                while True:
                    self.__controlador_sistema.controlador_passeio.listar_passeios()
                    adicionar = self.__tela_pacote.confirma_adicao("passeio")
                    if not adicionar:
                        break
                    
                    id_passeio = self.__tela_pacote.pega_id_passeio()
                    if not id_passeio:
                        continue

                    passeio = self.__controlador_sistema.controlador_passeio.buscar_por_id(id_passeio)
                    
                    if passeio:
                        pacote.adicionar_passeio(passeio)
                        self.__tela_pacote.mostra_mensagem("Passeio adicionado!")
                    else:
                        self.__tela_pacote.mostra_mensagem("Passeio não encontrado!")
            
            self.__pacotes_DAO.add(pacote)
            self.__proximo_id += 1
            
            self.__tela_pacote.mostra_mensagem(f"Pacote criado para o grupo '{grupo.nome}' com sucesso!")
        
        except Exception as e:
            self.__tela_pacote.mostra_mensagem(f"Erro ao criar pacote: {str(e)}")
    
    def listar_pacotes(self):
        """Lista todos os pacotes cadastrados"""
        pacotes = list(self.__pacotes_DAO.get_all())
        
        if not pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado no sistema.")
            return
        
        dados_pacotes = []
        for pacote in pacotes:
            dados_pacotes.append({
                'id': pacote.id,
                'grupo': pacote.grupo.nome,
                'total_passagens': len(pacote.passagens),
                'total_passeios': len(pacote.passeios),
                'valor_total': pacote.valor_total(),
                'valor_pago': pacote.calcular_valor_pago(),
                'valor_restante': pacote.calcular_valor_restante()
            })
        
        self.__tela_pacote.lista_pacotes(dados_pacotes)
    
    def alterar_pacote(self):
        """Altera um pacote existente"""
        pacotes = list(self.__pacotes_DAO.get_all())
        
        if not pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado.")
            return
        
        try:
            self.listar_pacotes()
            id_pacote = self.__tela_pacote.seleciona_pacote()
            
            pacote = self.buscar_por_id(id_pacote)
            
            if not pacote:
                self.__tela_pacote.mostra_mensagem("Pacote não encontrado!")
                return
            
            # Menu de alterações
            opcao = self.__tela_pacote.mostra_menu_alteracao()

            if opcao == 1:
                # Adicionar passagem
                if not self.__controlador_sistema.controlador_passagem.obter_todas_passagens():
                    self.__tela_pacote.mostra_mensagem("Nenhuma passagem cadastrada.")
                    return
                
                self.__controlador_sistema.controlador_passagem.listar_passagens()
                id_passagem = self.__tela_pacote.pega_id_passagem()
                if not id_passagem:
                    return
                
                passagem = self.__controlador_sistema.controlador_passagem.buscar_por_id(id_passagem)
                
                if passagem:
                    pacote.adicionar_passagem(passagem)
                    self.__pacotes_DAO.update(pacote)
                    self.__tela_pacote.mostra_mensagem("Passagem adicionada!")

                else:
                    self.__tela_pacote.mostra_mensagem("Passagem não encontrada!")
            
            elif opcao == 2:
                # Remover passagem
                if not pacote.passagens:
                    self.__tela_pacote.mostra_mensagem("Não há passagens no pacote.")
                    return
                
                print("\n--- PASSAGENS DO PACOTE ---")
                for passagem in pacote.passagens:
                    print(f"ID {passagem.id}: {passagem.origem} → {passagem.destino}\n")
                
                id_passagem = self.__tela_pacote.pega_id_passagem()
                if not id_passagem:
                    return

                passagem_encontrada = None
                
                for p in pacote.passagens:
                    if p.id == id_passagem:
                        passagem_encontrada = p
                        break
                
                if passagem_encontrada:
                    pacote.excluir_passagem(passagem_encontrada)
                    self.__pacotes_DAO.update(pacote)
                    self.__tela_pacote.mostra_mensagem("Passagem removida!")
                else:
                    self.__tela_pacote.mostra_mensagem("Passagem não encontrada!")
            
            elif opcao == 3:
                # Adicionar passeio
                if not self.__controlador_sistema.controlador_passeio.obter_passeios():
                    self.__tela_pacote.mostra_mensagem("Nenhum passeio cadastrado.")
                    return
                
                self.__controlador_sistema.controlador_passeio.listar_passeios()
                id_passeio = self.__tela_pacote.pega_id_passeio()
                if not id_passeio:
                    return

                passeio = self.__controlador_sistema.controlador_passeio.buscar_por_id(id_passeio)
                
                if passeio:
                    pacote.adicionar_passeio(passeio)
                    self.__pacotes_DAO.update(pacote)
                    self.__tela_pacote.mostra_mensagem("Passeio adicionado!")
                else:
                    self.__tela_pacote.mostra_mensagem("Passeio não encontrado!")
            
            elif opcao == 4:
                # Remover passeio
                if not pacote.passeios:
                    self.__tela_pacote.mostra_mensagem("Não há passeios no pacote.")
                    return
                
                print("\n--- PASSEIOS DO PACOTE ---")
                for passeio in pacote.passeios:
                    print(f"ID {passeio.id}: {passeio.atracao_turistica}\n")
                
                id_passeio = self.__tela_pacote.pega_id_passeio()
                if not id_passeio:
                    return

                passeio_encontrado = None
                
                for p in pacote.passeios:
                    if p.id == id_passeio:
                        passeio_encontrado = p
                        break
                
                if passeio_encontrado:
                    pacote.excluir_passeio(passeio_encontrado)
                    self.__pacotes_DAO.update(pacote)
                    self.__tela_pacote.mostra_mensagem("Passeio removido!")
                else:
                    self.__tela_pacote.mostra_mensagem("Passeio não encontrado!")
            
            elif opcao == 5:
                # Adicionar pagamento
                valor_restante = pacote.calcular_valor_restante()
                
                if valor_restante <= 0:
                    self.__tela_pacote.mostra_mensagem("O pacote já está totalmente pago!")
                    return
                
                print(f"\nValor total do pacote: R$ {pacote.valor_total():.2f}")
                print(f"Valor já pago: R$ {pacote.calcular_valor_pago():.2f}")
                print(f"Valor restante: R$ {valor_restante:.2f}")
                
                membros = pacote.grupo.membros
                
                if not membros:
                    self.__tela_pacote.mostra_mensagem("O grupo não possui membros!")
                    return
                
                print("\n--- MEMBROS DO GRUPO ---")
                for membro in membros:
                    print(f"{membro.id} - {membro.nome} (CPF: {membro.cpf})")
                
                try:
                    id_membro = self.__tela_pacote.seleciona_membro(membros)
                    pessoa = None
                    
                    for membro in membros:
                        if membro.id == id_membro:
                            pessoa = membro
                            break

                    if not pessoa:
                        self.__tela_pacote.mostra_mensagem("Membro não encontrado!")
                        return

                    pagamento = self.__controlador_sistema.controlador_pagamento.inicia(valor_restante, pessoa)
                    
                    if pagamento:
                        pacote.adicionar_pagamento(pagamento)
                        self.__pacotes_DAO.update(pacote)
                        self.__tela_pacote.mostra_mensagem("Pagamento registrado com sucesso!")

                    else:
                        self.__tela_pacote.mostra_mensagem("Pagamento cancelado.")

                except ValueError:
                    self.__tela_pacote.mostra_mensagem("Entrada inválida!")
            
            elif opcao == 0:
                self.__tela_pacote.mostra_mensagem("Operação cancelada.")
            else:
                self.__tela_pacote.mostra_mensagem("Opção inválida!")
        
        except Exception as e:
            self.__tela_pacote.mostra_mensagem(f"Erro ao alterar pacote: {str(e)}")
    
    def excluir_pacote(self):
        """Exclui um pacote"""
        pacotes = list(self.__pacotes_DAO.get_all())
        
        if not pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado.")
            return
        
        try:
            self.listar_pacotes()
            id_pacote = self.__tela_pacote.seleciona_pacote()

            pacote = self.buscar_por_id(id_pacote)

            if not pacote:
                self.__tela_pacote.mostra_mensagem("Pacote não encontrado!")
                return

            confirmacao = self.__tela_pacote.confirma_exclusao(pacote.grupo.nome)
            
            if confirmacao:
                self.__pacotes_DAO.remove(id_pacote)
                self.__tela_pacote.mostra_mensagem("Pacote excluído com sucesso!")
            else:
                self.__tela_pacote.mostra_mensagem("Exclusão cancelada.")
        
        except Exception as e:
            self.__tela_pacote.mostra_mensagem(f"Erro ao excluir pacote: {str(e)}")
    
    def sair(self):
        """Sai do menu de pacotes"""
        self.__tela_pacote.mostra_mensagem('Encerrando o gerenciamento de pacotes.')
        return True