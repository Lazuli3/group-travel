from entidades.pacote import Pacote
from view.tela_pacote import TelaPacote

class ControladorPacote:
    """Controlador para gerenciar pacotes de viagem"""
    
    def __init__(self, controlador_passagem_geral, controlador_passeio, 
                 controlador_grupo, controlador_pagamento):
        self.__pacotes = []
        self.__tela_pacote = TelaPacote()
        
        # Referências aos outros controladores
        self.controlador_passagem_geral = controlador_passagem_geral
        self.controlador_passeio_turistico = controlador_passeio
        self.controlador_grupo = controlador_grupo
        self.controlador_pagamento = controlador_pagamento
    
    def inicia(self):
        """Menu principal do controlador de pacotes"""
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
        """Cria um novo pacote"""
        try:
            # Verifica se há grupos cadastrados
            if not self.controlador_grupo._ControladorGrupo__grupos:
                self.__tela_pacote.mostra_mensagem("Nenhum grupo cadastrado. Cadastre um grupo primeiro!")
                return
            
            # Mostra grupos disponíveis
            print("\n--- GRUPOS DISPONÍVEIS ---")
            self.controlador_grupo.listar_grupos()
            
            # Seleciona grupo
            id_grupo = self.__tela_pacote.pega_id_grupo()
            grupo = self.controlador_grupo.buscar_por_id(id_grupo)
            
            if not grupo:
                self.__tela_pacote.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return
            
            # Cria pacote vazio para o grupo
            pacote = Pacote([], [], grupo)
            
            # Adiciona passagens (opcional)
            if self.controlador_passagem_geral._ControladorPassagem__passagens:
                print("\n--- ADICIONAR PASSAGENS ---")
                while True:
                    self.controlador_passagem_geral.listar_passagens()
                    adicionar = self.__tela_pacote.confirma_adicao("passagem")
                    if not adicionar:
                        break
                    
                    indice = self.__tela_pacote.pega_indice()
                    passagens_lista = self.controlador_passagem_geral._ControladorPassagem__passagens
                    
                    if 0 <= indice < len(passagens_lista):
                        pacote.adicionar_passagem(passagens_lista[indice])
                        self.__tela_pacote.mostra_mensagem("Passagem adicionada!")
                    else:
                        self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            # Adiciona passeios (opcional)
            if self.controlador_passeio_turistico._ControladorPasseioTuristico__passeios:
                print("\n--- ADICIONAR PASSEIOS ---")
                while True:
                    self.controlador_passeio_turistico.listar_passeios()
                    adicionar = self.__tela_pacote.confirma_adicao("passeio")
                    if not adicionar:
                        break
                    
                    indice = self.__tela_pacote.pega_indice()
                    passeios_lista = self.controlador_passeio_turistico._ControladorPasseioTuristico__passeios
                    
                    if 0 <= indice < len(passeios_lista):
                        pacote.adicionar_passeio(passeios_lista[indice])
                        self.__tela_pacote.mostra_mensagem("Passeio adicionado!")
                    else:
                        self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            self.__pacotes.append(pacote)
            self.__tela_pacote.mostra_mensagem(f"Pacote criado para o grupo '{grupo.nome}' com sucesso!")
        
        except Exception as e:
            self.__tela_pacote.mostra_mensagem(f"Erro ao criar pacote: {str(e)}")
    
    def listar_pacotes(self):
        """Lista todos os pacotes cadastrados"""
        if not self.__pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado no sistema.")
            return
        
        dados_pacotes = []
        for i, pacote in enumerate(self.__pacotes):
            dados_pacotes.append({
                'indice': i,
                'grupo': pacote.grupo().nome,
                'total_passagens': len(pacote.passagens()),
                'total_passeios': len(pacote.passeios()),
                'valor_total': pacote.valor_total(),
                'valor_pago': pacote.calcular_valor_pago(),
                'valor_restante': pacote.calcular_valor_restante()
            })
        
        self.__tela_pacote.lista_pacotes(dados_pacotes)
    
    def alterar_pacote(self):
        """Altera um pacote existente"""
        if not self.__pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado.")
            return
        
        try:
            self.listar_pacotes()
            indice = self.__tela_pacote.seleciona_pacote()
            
            if indice < 0 or indice >= len(self.__pacotes):
                self.__tela_pacote.mostra_mensagem("Índice inválido!")
                return
            
            pacote = self.__pacotes[indice]
            
            # Menu de alterações
            print("\n--- MENU ---")
            print("1 - Adicionar Passagem")
            print("2 - Remover Passagem")
            print("3 - Adicionar Passeio")
            print("4 - Remover Passeio")
            print("5 - Adicionar Pagamento")
            print("0 - Cancelar")
            
            try:
                opcao = int(input("Escolha: "))
            except ValueError:
                self.__tela_pacote.mostra_mensagem("Opção inválida!")
                return
            
            if opcao == 1:
                # Adicionar passagem
                if not self.controlador_passagem_geral._ControladorPassagem__passagens:
                    self.__tela_pacote.mostra_mensagem("Nenhuma passagem cadastrada.")
                    return
                
                self.controlador_passagem_geral.listar_passagens()
                idx = self.__tela_pacote.pega_indice()
                passagens = self.controlador_passagem_geral._ControladorPassagem__passagens
                
                if 0 <= idx < len(passagens):
                    pacote.adicionar_passagem(passagens[idx])
                    self.__tela_pacote.mostra_mensagem("Passagem adicionada!")
                else:
                    self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            elif opcao == 2:
                # Remover passagem
                if not pacote.passagens():
                    self.__tela_pacote.mostra_mensagem("Não há passagens no pacote.")
                    return
                
                print("\n--- PASSAGENS DO PACOTE ---")
                for i, p in enumerate(pacote.passagens()):
                    print(f"{i} - {p}")
                
                idx = self.__tela_pacote.pega_indice()
                if 0 <= idx < len(pacote.passagens()):
                    pacote.excluir_passagem(pacote.passagens()[idx])
                    self.__tela_pacote.mostra_mensagem("Passagem removida!")
                else:
                    self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            elif opcao == 3:
                if not self.controlador_passeio_turistico._ControladorPasseioTuristico__passeios:
                    self.__tela_pacote.mostra_mensagem("Nenhum passeio cadastrado.")
                    return
                
                self.controlador_passeio_turistico.listar_passeios()
                idx = self.__tela_pacote.pega_indice()
                passeios = self.controlador_passeio_turistico._ControladorPasseioTuristico__passeios
                
                if 0 <= idx < len(passeios):
                    pacote.adicionar_passeio(passeios[idx])
                    self.__tela_pacote.mostra_mensagem("Passeio adicionado!")
                else:
                    self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            elif opcao == 4:
                # Remover passeio
                if not pacote.passeios():
                    self.__tela_pacote.mostra_mensagem("Não há passeios no pacote.")
                    return
                
                print("\n--- PASSEIOS DO PACOTE ---")
                for i, p in enumerate(pacote.passeios()):
                    print(f"{i} - {p.atracao_turistica}")
                
                idx = self.__tela_pacote.pega_indice()
                if 0 <= idx < len(pacote.passeios()):
                    pacote.excluir_passeio(pacote.passeios()[idx])
                    self.__tela_pacote.mostra_mensagem("Passeio removido!")
                else:
                    self.__tela_pacote.mostra_mensagem("Índice inválido!")
            
            elif opcao == 5:
                # Adicionar pagamento
                valor_restante = pacote.calcular_valor_restante()
                
                if valor_restante <= 0:
                    self.__tela_pacote.mostra_mensagem("O pacote já está totalmente pago!")
                    return
                
                print(f"\nValor total do pacote: R$ {pacote.valor_total():.2f}")
                print(f"Valor já pago: R$ {pacote.calcular_valor_pago():.2f}")
                print(f"Valor restante: R$ {valor_restante:.2f}")
                
                # Pega os membros do grupo para escolher quem vai pagar
                membros = self.controlador_grupo.obter_membros(pacote.grupo().id)
                
                if not membros:
                    self.__tela_pacote.mostra_mensagem("O grupo não possui membros!")
                    return
                
                print("\n--- MEMBROS DO GRUPO ---")
                for i, membro in enumerate(membros):
                    print(f"{i} - {membro.nome} (CPF: {membro.cpf})")
                
                try:
                    idx_membro = int(input("\nEscolha o membro que fará o pagamento: "))
                    if 0 <= idx_membro < len(membros):
                        pessoa = membros[idx_membro]
                        
                        # Chama o controlador de pagamento
                        pagamento = self.controlador_pagamento.inicia(valor_restante, pessoa)
                        
                        if pagamento:
                            pacote.adicionar_pagamento(pagamento)
                            self.__tela_pacote.mostra_mensagem("Pagamento registrado com sucesso!")
                    else:
                        self.__tela_pacote.mostra_mensagem("Índice inválido!")
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
        if not self.__pacotes:
            self.__tela_pacote.mostra_mensagem("Nenhum pacote cadastrado.")
            return
        
        try:
            self.listar_pacotes()
            indice = self.__tela_pacote.seleciona_pacote()
            
            if indice < 0 or indice >= len(self.__pacotes):
                self.__tela_pacote.mostra_mensagem("Índice inválido!")
                return
            
            pacote = self.__pacotes[indice]
            confirmacao = self.__tela_pacote.confirma_exclusao(pacote.grupo().nome)
            
            if confirmacao:
                self.__pacotes.remove(pacote)
                self.__tela_pacote.mostra_mensagem("Pacote excluído com sucesso!")
            else:
                self.__tela_pacote.mostra_mensagem("Exclusão cancelada.")
        
        except Exception as e:
            self.__tela_pacote.mostra_mensagem(f"Erro ao excluir pacote: {str(e)}")
    
    def sair(self):
        """Sai do menu de pacotes"""
        self.__tela_pacote.mostra_mensagem('Encerrando o gerenciamento de pacotes.')
        return True