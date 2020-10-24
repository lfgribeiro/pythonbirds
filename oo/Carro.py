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
    0
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
    posicao = ('N', 'L', 'S', 'O')
    posicao_tupla = 0

    @classmethod
    def girar_a_direita(cls):
        cls.posicao_tupla += 1

    @classmethod
    def girar_a_esquerda(cls):
        cls.posicao_tupla -= 1


class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1

    @classmethod
    def frear(cls):
        if cls.velocidade > 0:
            cls.velocidade -= 1


class Carro:

    def __init__(self, mot, d):
        self.mot = mot
        self.d = d

    def calcular_velocidade(self):
        vel = self.mot
        return vel.velocidade

    def calcular_direcao(self):
        dire = self.d
        return dire.posicao[dire.posicao_tupla]


carro = Carro(mot=Motor(), d=Direcao())

