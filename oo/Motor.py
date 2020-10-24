class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1

    @classmethod
    def frear(cls):
        if cls.velocidade > 0:
            cls.velocidade -= 1

