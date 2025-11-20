class Grupo:
    
    def __init__(self, id_grupo, nome, descricao=""):
        self.__id = id_grupo
        self.__nome = nome
        self.__descricao = descricao
        self.__membros_cpf = []  # Lista de CPFs dos membros

    @property
    def id(self):
        return self.__id
    
    @property
    def membros_cpf(self):
        return self.__membros_cpf.copy()
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
  
    #MANIPULAÇÃO
    
    def adicionar_membro(self, cpf):
        """
        Adiciona um membro ao grupo
        Retorna True se adicionado com sucesso, False se já era membro
        """
        if cpf not in self.__membros_cpf:
            self.__membros_cpf.append(cpf)
            return True
        return False
    
    def remover_membro(self, cpf):
        """
        Remove um membro do grupo
        Retorna True se removido com sucesso, False se não era membro
        """
        if cpf in self.__membros_cpf:
            self.__membros_cpf.remove(cpf)
            return True
        return False
    
    def tem_membro(self, cpf):
        """Verifica se um CPF é membro do grupo"""
        return cpf in self.__membros_cpf
    
    def total_membros(self):
        """Retorna o total de membros do grupo"""
        return len(self.__membros_cpf)
    
    def obter_lista_membros(self):
        """
        Retorna a lista interna de membros (sem cópia)
        Use apenas quando precisar iterar sobre os membros
        """
        return self.__membros_cpf
    
    def limpar_membros(self):
        """Remove todos os membros do grupo"""
        self.__membros_cpf.clear()

    def __str__(self):
        return f"Grupo: {self.__nome} (ID: {self.__id}, Membros: {self.total_membros()})"
    
    def __repr__(self):
        return f"Grupo(id={self.__id}, nome='{self.__nome}', membros={self.total_membros()})"