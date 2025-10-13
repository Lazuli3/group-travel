from datetime import datetime
from entidades.passeio_turistico import PasseioTuristico
from view.tela_passeio import TelaPasseioTuristico

class ControladorPasseioTuristico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__passeios = []
        self.__tela_passeio = TelaPasseioTuristico()

    def inicia(self):
        switcher = {
            1: self.incluir_passeio,
            2: self.listar_passeios,
            3: self.excluir_passeio,
            0: self.sair
        }

        while True:
            opcao = self.__tela_passeio.mostra_opcoes()

            funcao_escolhida = switcher.get(
                opcao,
                lambda: self.__tela_passeio.mostra_mensagem(
                    'Opção inválida.'
                )
            )
            if funcao_escolhida() is True:
                break

    def busca_local(self, cidade: str, pais: str):
        locais = self.__controlador_sistema.controlador_local_viagem.obter_locais()

        for local in locais:
            if local.cidade.lower() == cidade.lower() and local.pais.lower() == pais.lower():
                return local

        return None
    
    def valida_local(self, cidade: str, pais: str):
        ''' Valida se o local passado pelo usuário existe'''
        local = self.busca_local(cidade, pais)
        if local is None:
            self.__tela_passeio.mostra_mensagem(f"Local não encontrado: {cidade}, {pais}")
            return None
        return local
    
    def valida_grupo(self, id_grupo):
        '''Valida se o id (e o grupo) passado pelo usuário existe'''
        try:
            id_int = int(id_grupo)
        except(ValueError, TypeError):
            self.__tela_passeio.mostra_mensagem(
                f'ID de grupo inválido: {id_grupo}'
            )
            return None
        
        grupo = self.__controlador_sistema.controlador_grupo.buscar_por_id(id_int)
        if grupo is None:
            self.__tela_passeio.mostra_mensagem(f"Grupo com ID {id_int} não encontrado.")
            return None
        return grupo
    
    def valida_data_hora(self, dia: str, horario_inicio: str, horario_fim: str):
        """Valida e converte data/hora"""
        try:
            # strptime: método que converte uma string de data e hora em um objeto datetime
            data_inicio = datetime.strptime(f"{dia} {horario_inicio}", "%d/%m/%Y %H:%M")
            data_fim = datetime.strptime(f"{dia} {horario_fim}", "%d/%m/%Y %H:%M")

            if data_fim <= data_inicio:
                self.__tela_passeio.mostra_mensagem("Erro: horário de fim deve ser após o início!")
                return None, None

            return data_inicio, data_fim

        except ValueError:
            self.__tela_passeio.mostra_mensagem("Data ou horário em formato inválido!")
            return None, None

    def valida_valor(self, valor_str):
        try:
            valor = float(valor_str.replace(',', '.'))
            #se o usuário passou um valor com vírgula, substitui por . (float)

            if valor < 0:
                self.__tela_passeio.mostra_mensagem("Valor não pode ser negativo!")
                return None

            return valor

        except ValueError:
            self.__tela_passeio.mostra_mensagem("Valor inválido! Digite um número.")
            return None
   
    def incluir_passeio(self):
        while True:
            dados = self.__tela_passeio.pega_dados_passeio()

            if dados is None:
                return

            # Validação dos campos
            local = self.valida_local(dados['cidade'], dados['pais'])
            if local is None:
                continue
            
            grupo = self.valida_grupo(dados['id_grupo'])
            if grupo is None:
                continue
            
            data_inicio, data_fim = self.valida_data_hora(
                dados['dia'],
                dados['horario_inicio'],
                dados['horario_fim']
            )
            if data_inicio is None:
                continue
            
            valor = self.valida_valor(dados['valor'])
            if valor is None:
                continue

            # Criação do passeio
            try:
                novo = PasseioTuristico(
                    localizacao=local,
                    atracao_turistica=dados['atracao_turistica'],
                    horario_inicio=data_inicio,
                    horario_fim=data_fim,
                    valor=valor,
                    grupo_passeio=grupo
                )
                self.__passeios.append(novo)
                self.__tela_passeio.mostra_mensagem('Passeio turístico cadastrado com sucesso!')
                break
            
            except ValueError as e: 
                # e mostra o erro específico no construtor(raise ValueError)
                self.__tela_passeio.mostra_mensagem(f"Erro ao criar passeio: {e}")

    def obter_passeios(self):
        '''Retorna a lista de passeios, mas sem exibir'''
        return self.__passeios
    
    def passeios_para_dict(self):
        '''Converte passseios em uma lista de dicionários'''
        passeios_dict = []
        for passeio in self.__passeios:
            novo_dict = {
                'localizacao': f"{passeio.localizacao.cidade}, {passeio.localizacao.pais}",
                'atracao': passeio.atracao_turistica,
                'horario_inicio': passeio.horario_inicio.strftime("%d/%m/%Y %H:%M"),
                'horario_fim': passeio.horario_fim.strftime("%d/%m/%Y %H:%M"),
                'valor': f"R$ {passeio.valor:.2f}",
                'grupo': passeio.grupo_passeio.nome
            }
            passeios_dict.append(novo_dict)
        return passeios_dict

    def listar_passeios(self):
        if not self.__passeios:
            self.__tela_passeio.mostra_mensagem('Nenhum passeio turístico cadastrado.')
        else:
            self.__tela_passeio.lista_passeios_turisticos(self.passeios_para_dict())

    def excluir_passeio(self):
        if not self.__passeios:
            return
        
        indice = self.__tela_passeio.seleciona_passeio(self.passeios_para_dict())

        if indice is None:
            return
        
        passeio_excluido = self.__passeios[indice]
        del self.__passeios[indice]
        self.__tela_passeio.mostra_mensagem(
            f'''Passeio para atração turística '{passeio_excluido.atracao_turistica}'
            do grupo '{passeio_excluido.grupo_passeio.nome}' excluído com sucesso.'''
        )
        
    def sair(self):
        self.__tela_passeio.mostra_mensagem('Encerrando o cadastro.')
        return True
