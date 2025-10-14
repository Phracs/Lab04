class Passeggeri:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina_assegnata=None
    def __str__(self):
        return f"{self.codice} {self.nome} {self.cognome}