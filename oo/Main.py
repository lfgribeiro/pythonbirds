"""
Exemplo:

    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>>

"""


class Direcao:
    posicao = ('Norte', 'Leste', 'Sul', 'Oeste')
    posicao_tupla = 0
    valor = posicao[posicao_tupla]

    @classmethod
    def girar_a_direita(cls):
       cls.posicao_tupla += 1
       cls.valor = cls.posicao[cls.posicao_tupla % len(cls.posicao)]

    @classmethod
    def girar_a_esquerda(cls):
            cls.posicao_tupla -= 1
            cls.valor = cls.posicao[cls.posicao_tupla % len(cls.posicao)]

class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1


    @classmethod
    def frear(cls):
        cls.velocidade -= 1
        #se o valor for menor que 0, coloca o 0 como maior valor
        cls.velocidade = max(0, cls.velocidade)


class Carro:

    def __init__(self, d, mot):
        self.mot = mot
        self.d = d

    def calcular_velocidade(self):
        vel = self.mot.velocidade
        return vel

    def calcular_direcao(self):
        dire = self.d.valor
        return dire

    def acelerar(self):
        self.mot.acelerar()

    def frear(self):
        self.mot.frear()

    def girar_a_direita(self):
        self.d.girar_a_direita()

    def girar_a_esquerda(self):
        self.d.girar_a_esquerda()