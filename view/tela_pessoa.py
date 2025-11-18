import FreeSimpleGUI as sg

class TelaPessoa:
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
            self.close()
        return opcao

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- PESSOAS ----------', font=("Comic Sans", 25))],
            [sg.Text('Escolha sua opção', font=("Comic Sans", 15))],
            [sg.Radio('Incluir Amigo', "RD1", key='1')],
            [sg.Radio('Alterar Amigo', "RD1", key='2')],
            [sg.Radio('Listar Amigos', "RD1", key='3')],
            [sg.Radio('Excluir Amigo', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de pessoa').Layout(layout)

    def pega_dados_pessoa(self):
        print('============ Cadastro ============')
        nome = str(input('Nome: '))
        try:
            idade = int(input('Idade: '))
        except ValueError:
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