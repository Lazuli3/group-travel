from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
    @abstractmethod
    def __init__ (self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        ids = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasouce, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    def gerar_id(self):
        id = 0
        for i in self.ids:
            if i == id:
                id +=1
        self.ids.append(id)
        return id