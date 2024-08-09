
class CalculaCorrida:
    def __init__(self, km, preco_km=5):
        self.km = km
        self.preco_km = preco_km

    def get_valor(self):
        return self.km * self.preco_km

class CalculaCorridaUberX(CalculaCorrida):
    def get_valor(self):
        return 0.9 * super().get_valor()

class CalculaCorridaUberMoto(CalculaCorrida):
    def get_valor(self):
        return 1.1 * super().get_valor()

class CalculaCorridaUberBlack(CalculaCorrida):
    def get_valor(self):
        return super().get_valor()

class CalculaCorridaUberPool(CalculaCorrida):
    def __init__(self, km, preco_km=5, passageiros=1):
        super().__init__(km, preco_km)
        self.passageiros = passageiros

    def get_valor(self):
        return super().get_valor() / self.passageiros