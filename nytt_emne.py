from data import emner
from emne import Emne

def lag_nytt_emne():
    emnekode = input("Skriv inn emnekode f.eks. DAT120: ").upper()
    navn = input("Skriv inn emnenavn: ")
    semester = input("Skriv inn semester tid H(øst)/V(år): ").upper()
    studiepoeng = int(input("Skriv inn studiepoeng: "))

    nytt_emne = Emne(emnekode, navn, semester, studiepoeng)
    emner.append(nytt_emne)

    print(f"Emne {emnekode} ({semester}, {studiepoeng} studiepoeng) lagt til.\n")
