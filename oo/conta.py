
# Classe
class Conta:

    # Função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        # Definição dos atributos
        self.__numero = numero # __ faz com que o atributo se torne PRIVADO
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos do obj Conta (SELF é utilizado para acessar os atributos)
    def extrato(self):
        print("Saldo {} do(a) titular {} ".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # Métodos privados não podem ser acessados de forma direta
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite ".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    # @property permite o acesso direto a consulta da função
    @property
    def limite(self):
        return self.__limite
    # @limite.setter permite setar a função e modificar o atributo
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # @staticmethod representa métodos estáticos
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_banco():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}

