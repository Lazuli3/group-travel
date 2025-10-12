from datetime import datetime

class TelaPassagemGeral:
    
    def mostra_opcoes(self):
        """Exibe o menu de opções e retorna a escolha do usuário"""
        print("\n" + "="*60)
        print("     GERENCIAMENTO DE VIAGENS")
        print("="*60)
        print("EMPRESAS:")
        print("  1 - Cadastrar Empresa")
        print("  2 - Listar Empresas")
        print("  3 - Excluir Empresa")
        print("\nTRANSPORTES:")
        print("  4 - Cadastrar Transporte")
        print("  5 - Listar Transportes")
        print("  6 - Excluir Transporte")
        print("\nPASSAGENS:")
        print("  7 - Cadastrar Passagem")
        print("  8 - Listar Passagens")
        print("  9 - Excluir Passagem")
        print("\n  0 - Voltar")
        print("="*60)
        
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1
    
    #EMPRESA
    
    def pega_dados_empresa(self):
        print("\n--- CADASTRO DE EMPRESA ---")
        nome = input("Nome da empresa: ").strip()
        cnpj = input("CNPJ: ").strip()
        telefone = input("Telefone: ").strip()
        
        return {
            'nome': nome,
            'cnpj': cnpj,
            'telefone': telefone
        }
    
    def pega_cnpj(self):
        cnpj = input("\nDigite o CNPJ da empresa: ").strip()
        return cnpj
    
    def lista_empresas(self, empresas):
        print("\n" + "="*80)
        print("     EMPRESAS CADASTRADAS")
        print("="*80)
        print(f"{'Nome':<30} {'CNPJ':<20} {'Telefone':<15}")
        print("-"*80)
        
        for empresa in empresas:
            print(f"{empresa.nome:<30} {empresa.cnpj:<20} {empresa.telefone:<15}")
        
        print("="*80)
    
    #TRANSPORTE
    
    def pega_dados_transporte(self):
        print("\n--- CADASTRO DE TRANSPORTE ---")
        tipo = input("Tipo de transporte (Ônibus/Avião/Van/etc): ").strip()
        cnpj_empresa = input("CNPJ da empresa: ").strip()
        
        return {
            'tipo': tipo,
            'cnpj_empresa': cnpj_empresa
        }
    
    def seleciona_transporte(self):
        try:
            indice = int(input("\nDigite o número do transporte: "))
            return indice
        except ValueError:
            self.mostra_mensagem("Número inválido!")
            return -1
    
    def lista_transportes(self, transportes):
        print("\n" + "="*80)
        print("     TRANSPORTES CADASTRADOS")
        print("="*80)
        print(f"{'Nº':<5} {'Tipo':<20} {'Empresa':<30} {'CNPJ':<20}")
        print("-"*80)
        
        for i, transporte in enumerate(transportes):
            print(f"{i:<5} {transporte.tipo:<20} {transporte.empresa.nome:<30} {transporte.empresa.cnpj:<20}")
        
        print("="*80)
    
    #PASSAGEM
    
    def pega_dados_passagem(self, controlador_local_viagem):
        print("\n--- CADASTRO DE PASSAGEM ---")

        print("\nData da viagem:")
        dia = int(input("  Dia: "))
        mes = int(input("  Mês: "))
        ano = int(input("  Ano: "))
        data = datetime(ano, mes, dia)
        
        valor = float(input("\nValor da passagem (R$): "))

        print("\n--- SELECIONE A ORIGEM ---")
        locais = controlador_local_viagem._ControladorLocalViagem__locais_viagem
        indice_origem = controlador_local_viagem._ControladorLocalViagem__tela_local_viagem.seleciona_local(locais)
        
        if indice_origem is None:
            return None  # Usuário cancelou
        
        local_origem = locais[indice_origem]
        
        print("\n--- SELECIONE O DESTINO ---")
        indice_destino = controlador_local_viagem._ControladorLocalViagem__tela_local_viagem.seleciona_local(locais)
        
        if indice_destino is None:
            return None  # Usuário cancelou
        
        local_destino = locais[indice_destino]
        indice_transporte = int(input("\nNúmero do transporte: "))
        
        return {
            'data': data,
            'valor': valor,
            'local_origem': local_origem,
            'local_destino': local_destino,
            'indice_transporte': indice_transporte
        }
    
    def seleciona_passagem(self):
        try:
            indice = int(input("\nDigite o número da passagem: "))
            return indice
        except ValueError:
            self.mostra_mensagem("Número inválido!")
            return -1
    
    def lista_passagens(self, passagens):
        print("\n" + "="*100)
        print("     PASSAGENS CADASTRADAS")
        print("="*100)
        print(f"{'Nº':<5} {'Data':<12} {'Origem':<25} {'Destino':<25} {'Transporte':<20} {'Valor':<10}")
        print("-"*100)
        
        for i, passagem in enumerate(passagens):
            data_formatada = passagem.data.strftime("%d/%m/%Y")
            origem = f"{passagem.local_origem.cidade}/{passagem.local_origem.pais}"
            destino = f"{passagem.local_destino.cidade}/{passagem.local_destino.pais}"
            transporte = f"{passagem.transporte.tipo}"
            valor = f"R$ {passagem.valor:.2f}"
            
            print(f"{i:<5} {data_formatada:<12} {origem:<25} {destino:<25} {transporte:<20} {valor:<10}")
        
        print("="*100)
        
    def mostra_mensagem(self, msg:str):
        print(f"\n>>> {msg}")
        input("Pressione ENTER para continuar.")