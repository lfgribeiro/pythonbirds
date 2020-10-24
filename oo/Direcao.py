class Direcao:
    posicao = ('N', 'L', 'S', 'O')
    posicao_tupla = 0

    @classmethod
    def girar_a_direita(cls):
        cls.posicao_tupla += 1

    @classmethod
    def girar_a_esquerda(cls):
        cls.posicao_tupla -= 1

