import Cabina
import Passeggeri
import csv

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabine={}
        self.passeggeri={}

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader=csv.reader(infile)
                for row in reader:
                    if row and row[0].startswith("CAB"):
                        if len(row) == 4:
                            codice = row[0]
                            num_letti = row[1]
                            ponte = row[2]
                            prezzo = row[3]
                            cab=Cabina.Cabine(codice, int(num_letti), int(ponte), float(prezzo))
                            self.cabine[codice] = cab
                        if len(row) == 5:
                            codice, num_letti, ponte, prezzo, extra = row
                            try:
                                num_animali = int(extra)
                                cab = Cabina.Cabina_Animali(codice, int(num_letti), int(ponte), float(prezzo), num_animali)
                            except ValueError:
                                stile=extra
                                cab = Cabina.Cabina_Deluxe(codice, int(num_letti), int(ponte), float(prezzo), stile)
                            self.cabine[codice] = cab
                    elif row and row[0].startswith("P"):
                        codice = row[0]
                        nome= row[1]
                        cognome= row[2]
                        pas=Passeggeri.Passeggeri(codice, nome, cognome)
                        self.passeggeri[codice] = pas
        except FileNotFoundError:
            raise FileNotFoundError("File not found")



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        if codice_cabina not in self.cabine:
            raise KeyError(f"Non esiste una cabina con questo codice")
        if codice_passeggero not in self.passeggeri:
            raise KeyError(f"Non esiste una passeggero con questo codice")
        cab=self.cabine[codice_cabina]
        if cab.occupata is True:
            raise ValueError("Cabina assegnata")
        pas=self.passeggeri[codice_passeggero]
        if pas.cabina_assegnata is not None:
            raise ValueError("Passeggero assegnato")
        pas.cabina_assegnata=cab.codice
        cab.occupata=True



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabine=list(self.cabine.values())
        cabine_ordinate=sorted(cabine, key=lambda a: a.prezzo_finale())
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self.passeggeri.values():
            if p.cabina_assegnata is not None:
                print(f"{p.codice} {p.nome} {p.cognome} | Cabina:{p.cabina_assegnata}")
            if p.cabina_assegnata is None:
                print(f"{p.codice} {p.nome} {p.cognome} | Cabina: nessuna")