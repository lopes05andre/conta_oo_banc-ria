
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # @property -> se referete a uma propriedade
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()
    @nome.setter
    def nome(self, nome):
        print("Chamando @property nome()")
        self.__nome = nome