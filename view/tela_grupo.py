class TelaGrupo:
    def mostra_opcoes(self):
        """Exibe o menu de opções e retorna a escolha do usuário"""
        print("\n" + "="*50)
        print("     GERENCIAMENTO DE GRUPOS")
        print("="*50)
        print("1 - Criar Grupo")
        print("2 - Listar Grupos")
        print("3 - Adicionar Pessoa ao Grupo")
        print("4 - Listar Pessoas do Grupo")
        print("5 - Remover Pessoa do Grupo")
        print("6 - Excluir Grupo")
        print("0 - Voltar")
        print("="*50)
        
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_grupo(self):
        print("\n--- CADASTRO DE GRUPO ---")
        nome = input("Nome do grupo: ").strip()
        descricao = input("Descrição (opcional): ").strip()
        
        return {
            'nome': nome,
            'descricao': descricao if descricao else ""
        }

    def seleciona_grupo(self):
        try:
            id_grupo = int(input("\nDigite o ID do grupo: "))
            return id_grupo
        except ValueError:
            self.mostra_mensagem("ID inválido!")
            return None

    def pega_cpf_pessoa(self):
        cpf = input("\nDigite o CPF da pessoa: ").strip()
        return cpf

    def lista_grupos(self, grupos):
        print("     GRUPOS CADASTRADOS")
        print("="*70)
        print(f"{'ID':<5} {'Nome':<25} {'Membros':<10} {'Descrição':<30}")
        print("-"*70)
        
        for grupo in grupos:
            print(f"{grupo['id']:<5} {grupo['nome']:<25} {grupo['total_membros']:<10} {grupo['descricao']:<30}")
        
        print("="*70)

    def lista_membros(self, nome_grupo, membros):
        print("\n" + "="*80)
        print(f"     MEMBROS DO GRUPO: {nome_grupo}")
        print("="*80)
        print(f"{'Nome':<30} {'CPF':<20} {'Telefone':<15}")
        print("-"*80)
        
        for membro in membros:
            print(f"{membro['nome']:<30} {membro['cpf']:<20} {membro['telefone']:<15}")
        
        print("="*80)

    def confirma_exclusao(self, nome_grupo):
        print(f"\nVocê confirma a exclusão do grupo: '{nome_grupo}'")
        print("Todos os membros serão desvinculados deste grupo.")
        resposta = input("Certeza que quer excluir? (S/N): ").strip().upper()
        return resposta == 'S'

    def mostra_mensagem(self, msg:str):
        print(f"\n>>> {msg}")
        input("Pressione a tecla ENTER para continuar.")