
class TelaPessoa:

    def mostra_opcoes(self):
        print('============ Menu ============')
        print("1 - Incluir pessoa")
        print('2 - Listar pessoas')
        print('3 - Excluir pessoa')
        print('0 - Sair')

        try:
            return int(input('Escolha uma das opções do menu: '))
        
        except TypeError:
            self.mostra_mensagem("Escolha uma opção válida do menu, intervado de [0,1,2,3].")

    def pega_dados_pessoa(self):
        print('============ Cadastro ============')
        nome = str(input('Nome: '))
        try:
            idade = int(input('Idade: '))
        except TypeError:
            self.mostra_mensagem("A idade tem que ser um valor inteiro para ser válido.")
            idade = 0
        telefone = str(input('Telefone: '))
        cpf = str(input('CPF: '))
        return {
            'nome': nome,
            'idade': idade,
            'telefone': telefone,
            'cpf': cpf 
        }
    
    def lista_pessoas(self, pessoas:list):
        print('============ Lista de pessoas ============')
        for p in pessoas:
            print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cpf: {p.cpf}")

    def pega_cpf(self):
        return input('Digite o cpf da pessoa: ')
    
    def mostra_mensagem(self, msg:str):
        print(msg)