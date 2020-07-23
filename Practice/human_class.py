class Mard:
    def __init__(self, anun, azganun, tariq):
        self.anun = anun
        self.azganun = azganun
        self.tariq = tariq

    def __str__(self):
        return "{} {} {}".format(self.anun, self.azganun, self.tariq)


Narek = Mard("Narek", "Ikhtiaryan", "27")

print(Narek)
