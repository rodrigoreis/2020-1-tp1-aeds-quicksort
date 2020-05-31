class Item:

    def __init__ (self, site, classificacao):
        self.site = site
        self.classificacao = classificacao
        self.inicial = str.upper(site[0])

    def linha(self):
        return f'{self.site};{self.classificacao}'

    def __str__ (self):
        return f'Classificação: {self.classificacao}, Site: ({self.inicial}={ord(self.inicial)}) {self.site}'