
class Data:
    def __init__(self, dia, mes, ano):
        print(f'Contruindo objeto...{self}')
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
