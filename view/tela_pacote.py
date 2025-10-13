class TelaPacote:
    """Classe responsável pela interface de pacotes"""
    
    def mostra_opcoes(self):
        """Exibe o menu de opções"""
        print("\n" + "="*50)
        print("     GERENCIAMENTO DE PACOTES")
        print("="*50)
        print("1 - Incluir Pacote")
        print("2 - Listar Pacotes")
        print("3 - Alterar Pacote")
        print("4 - Excluir Pacote")
        print("0 - Voltar")
        print("="*50)
        
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1
    
    def pega_id_grupo(self):
        """Pede o ID do grupo"""
        try:
            id_grupo = int(input("\nDigite o ID do grupo: "))
            return id_grupo
        except ValueError:
            return -1
    
    def pega_indice(self):
        """Pede um índice"""
        try:
            indice = int(input("\nDigite o número: "))
            return indice
        except ValueError:
            return -1
    
    def confirma_adicao(self, tipo):
        """Confirma se deseja adicionar item"""
        resposta = input(f"\nDeseja adicionar {tipo}? (S/N): ").strip().upper()
        return resposta == 'S'
    
    def seleciona_pacote(self):
        """Pede ao usuário para selecionar um pacote"""
        try:
            indice = int(input("\nDigite o número do pacote: "))
            return indice
        except ValueError:
            return -1
    
    def lista_pacotes(self, pacotes):
        """Exibe a lista de pacotes"""
        print("\n" + "="*90)
        print("     PACOTES CADASTRADOS")
        print("="*90)
        print(f"{'Nº':<5} {'Grupo':<20} {'Passagens':<12} {'Passeios':<10} {'Total':<12} {'Pago':<12} {'Restante'}")
        print("-"*90)
        
        for pacote in pacotes:
            indice = pacote['indice']
            grupo = pacote['grupo'][:19]
            passagens = pacote['total_passagens']
            passeios = pacote['total_passeios']
            total = f"R$ {pacote['valor_total']:.2f}"
            pago = f"R$ {pacote['valor_pago']:.2f}"
            restante = f"R$ {pacote['valor_restante']:.2f}"
            
            print(f"{indice:<5} {grupo:<20} {passagens:<12} {passeios:<10} {total:<12} {pago:<12} {restante}")
        
        print("="*90)
    
    def confirma_exclusao(self, nome_grupo):
        """Confirma a exclusão de um pacote"""
        print(f"\n⚠️  Deseja excluir o pacote do grupo '{nome_grupo}'?")
        resposta = input("Confirma a exclusão? (S/N): ").strip().upper()
        return resposta == 'S'
    
    def mostra_mensagem(self, mensagem):
        """Exibe uma mensagem na tela"""
        print(f"\n>>> {mensagem}")
        input("Pressione ENTER para continuar...")