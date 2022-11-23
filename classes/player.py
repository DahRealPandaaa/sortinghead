class player:
    def __init__(self):
        self.naam = str
        self.punten_se = 0
        self.punten_fict = 0
        self.punten_de = 0
        self.punten_iat = 0
        # een set zodat er geen dubbele kenmerken worden opgeslagen
        self.kenmerken = set()
        self.running = False

    def set_score(self, se, fict, iat, de):
        self.punten_se = se + self.punten_se
        self.punten_fict = fict + self.punten_fict
        self.punten_de = de + self.punten_de
        self.punten_iat = iat + self.punten_iat

    def reset(self):
        self.punten_se = 0
        self.punten_fict = 0
        self.punten_de = 0
        self.punten_iat = 0
        self.kenmerken = set()
        self.running = False
