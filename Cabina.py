class Cabine:
    def __init__(self, codice, num_letti, ponte, prezzo):
        self.codice= codice
        self.num_letti=num_letti
        self.ponte=ponte
        self.prezzo=prezzo
    def prezzo_finale(self):
        return self.prezzo
    def __str__(self):
        return f"{self.codice} {self.num_letti} {self.ponte} {self.prezzo}"
class Cabina_Animali(Cabine):
    def __init__(self, codice, num_letti, ponte, prezzo, num_animali):
        super().__init__(codice, num_letti, ponte, prezzo)
        self.num_animali= num_animali

    def prezzo_finale(self):
        return self.prezzo*(1 + 0.10 * self.num_animali)
    def __str__(self):
        return f"{self.codice} {self.num_letti} {self.ponte} {self.prezzo} {self.num_animali}"

class Cabina_Deluxe(Cabine):
    def __init__(self, codice, num_letti, ponte, prezzo, stile):
        super().__init__(codice,num_letti,ponte,prezzo)
        self.stile=stile

    def prezzo_finale(self):
        return self.prezzo * 1.20
    def __str__(self):
        return f"{self.codice} {self.num_letti} {self.ponte} {self.prezzo} {self.stile}"