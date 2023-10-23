class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        print(f'chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print(f'chamando setter nome()')
        self.__nome = nome
        