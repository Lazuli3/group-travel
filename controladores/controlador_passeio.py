from datetime import datetime
from entidades.passeio_turistico import PasseioTuristico
from view.tela_passeio import TelaPasseioTuristico
from DAOs.passeio_dao import PasseioTuristicoDAO

class ControladorPasseioTuristico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__passeios_DAO = PasseioTuristicoDAO()
        self.__tela_passeio = TelaPasseioTuristico()
        self.__proximo_id = self.__gerar_proximo_id()

    def __gerar_proximo_id(self):
        """Gera o próximo ID disponível baseado nos locais existentes"""
        passeios = list(self.__passeios_DAO.get_all())
        if not passeios:
            return 1
        
        max_id = max(passeio.id for passeio in passeios)
        return max_id + 1
    
    def buscar_por_id(self, passeio_id):
        return self.__passeios_DAO.get(passeio_id)
    
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
        """Busca um local de viagem pelo nome da cidade e país"""
        # CORREÇÃO: Usa o método obter_locais() ao invés de tentar acessar propriedade inexistente
        locais = self.__controlador_sistema.controlador_local_viagem.obter_locais()

        for local in locais:
            if local.cidade.lower() == cidade.lower() and local.pais.lower() == pais.lower():
                return local

        return None
    
    def valida_local(self, cidade: str, pais: str):
        """Valida se o local passado pelo usuário existe"""
        local = self.busca_local(cidade, pais)
        if local is None:
            self.__tela_passeio.mostra_mensagem(f"Local não encontrado: {cidade}, {pais}")
            return None
        return local
    
    def valida_grupo(self, id_grupo):
        """Valida se o id (e o grupo) passado pelo usuário existe"""
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
        """Valida e converte o valor para float"""
        try:
            valor = float(valor_str.replace(',', '.'))
            # Se o usuário passou um valor com vírgula, substitui por . (float)

            if valor < 0:
                self.__tela_passeio.mostra_mensagem("Valor não pode ser negativo!")
                return None

            return valor

        except ValueError:
            self.__tela_passeio.mostra_mensagem("Valor inválido! Digite um número.")
            return None
   
    def incluir_passeio(self):
        """Cadastra um novo passeio turístico"""
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
                    id=self.__proximo_id,
                    localizacao=local,
                    atracao_turistica=dados['atracao_turistica'],
                    horario_inicio=data_inicio,
                    horario_fim=data_fim,
                    valor=valor,
                    grupo_passeio=grupo
                )
                self.__passeios_DAO.add(novo)
                self.__proximo_id += 1
                self.__tela_passeio.mostra_mensagem('Passeio turístico cadastrado com sucesso!')
                break
            
            except ValueError as e: 
                # e mostra o erro específico no construtor(raise ValueError)
                self.__tela_passeio.mostra_mensagem(f"Erro ao criar passeio: {e}")

    def obter_passeios(self):
        """Retorna a lista de passeios, mas sem exibir"""
        return list(self.__passeios_DAO.get_all())
    
    def passeios_para_dict(self):
        """Converte passeios em uma lista de dicionários"""
        passeios_dict = []
        passeios = list(self.__passeios_DAO.get_all())

        for passeio in passeios:
            novo_dict = {
                'id': passeio.id,
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
        """Lista todos os passeios cadastrados"""
        passeios = list(self.__passeios_DAO.get_all())
        
        if not passeios:
            self.__tela_passeio.mostra_mensagem('Nenhum passeio turístico cadastrado.')
        else:
            self.__tela_passeio.lista_passeios_turisticos(self.passeios_para_dict())

    def excluir_passeio(self):
        """Exclui um passeio turístico"""
        passeios = list(self.__passeios_DAO.get_all())
        
        if not passeios:
            self.__tela_passeio.mostra_mensagem("Nenhum passeio cadastrado.")
            return
        
        try:
            self.listar_passeios()
            
            id_passeio = self.__tela_passeio.seleciona_passeio()
            passeio = self.buscar_por_id(id_passeio)

            if not passeio:
                self.__tela_passeio.mostra_mensagem(f"Passeio com ID {id_passeio} não encontrado!")
                return

            confirmacao = self.__tela_passeio.confirma_exclusao(
                passeio.atracao_turistica, 
                passeio.grupo_passeio.nome
            )
            if not confirmacao:
                self.__tela_passeio.mostra_mensagem("Exclusão cancelada.")
                return

            self.__passeios_DAO.remove(id_passeio)

            self.__tela_passeio.mostra_mensagem(
                f"Passeio '{passeio.atracao_turistica}' do grupo '{passeio.grupo_passeio.nome}' excluído com sucesso!"
            )
        
        except Exception as e:
            self.__tela_passeio.mostra_mensagem(f"Erro ao excluir passeio: {str(e)}")
        
    def sair(self):
        """Sai do menu de passeios"""
        self.__tela_passeio.mostra_mensagem('Encerrando o cadastro.')
        return True