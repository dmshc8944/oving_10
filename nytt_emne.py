from data import emner
from emne import Emne

def lag_nytt_emne():
    try:
        emnekode = input("Skriv inn emnekode f.eks. DAT120: ").upper()
        navn = input("Skriv inn emnenavn: ")
        semester = input("Skriv inn semester tid H(øst)/V(år): ").upper()
        studiepoeng = int(input("Skriv inn studiepoeng: "))

        # Валидация ввода
        if semester not in ['H', 'V']:
            print("Semester må være 'H' eller 'V'")
            return
        
        if studiepoeng <= 0:
            print("Studiepoeng må være positivt tall")
            return

        nytt_emne = Emne(emnekode, navn, semester, studiepoeng)
        emner.append(nytt_emne)

        print(f"Emne {emnekode} ({semester}, {studiepoeng} studiepoeng) lagt til.\n")
        return nytt_emne
    except ValueError:
        print("Studiepoeng må være et tall!")
        return None