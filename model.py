import random

STEVILO_DOVOLJENIH_NAPAK = 10    
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke == None else crke

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka  not in self.geslo:
                napacne.append(crka) 
        return napacne 

    def pravilne_crke(self):
        pravilne = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        napake = len(self.napacne_crke())
        return napake

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True
            
    def poraz(self):
        if len(self.napacne_crke()) >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else: return False

    def pravilni_del_gesla(self):
        pravilno = ""
        for crka in self.geslo:
            if crka in self.crke:
                pravilno += crka + " "
            else: pravilno += "_ "
        return pravilno

    def nepravilni_ugibi(self):
        nepravilni_ugibi = ""
        for crka in self.crke:
            if crka in self.napacne_crke():
                nepravilni_ugibi += crka  + " "
        return nepravilni_ugibi

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            if crka not in self.geslo():
                if self.poraz():
                    return PORAZ
                else: return  NAPACNA_CRKA
            if self.zmaga():
                return ZMAGA
            else: return PRAVILNA_CRKA

bazen_besed = []
with open("besede.txt", "r") as f:
    for vrstica in f:
        bazen_besed.append(vrstica)

#random.choise

def nova_igra():
    return Igra(random.choice(bazen_besed))






                   
        

