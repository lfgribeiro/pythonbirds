class Pessoa:
    olhos = 2

    def __init__(self, *filhos,nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    leticia = Pessoa("Letícia")
    luis = Pessoa(leticia, nome='Luis')
    print(Pessoa.cumprimentar(luis))
    print(id(luis))
    print(luis.cumprimentar())
    print(luis.nome)
    luis.nome = 'Filippe'
    print(luis.nome)
    print(luis.idade)
    for filho in luis.filhos:
        print(filho.nome)
    luis.sobrenome = 'Ribeiro'
    del luis.filhos
    print(luis.__dict__)
    print(leticia.__dict__)
