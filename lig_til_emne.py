from data import emner, studieplan




def sjekk_studiepoeng(emne, semester):
    """
    Sjekker om total studiepoeng i semester + dette emnet overstiger 30.
    Returnerer True hvis det er for mye, ellers False.
    """
    semester_index = semester - 1
    total_studiepoeng = sum(e.studiepoeng for e in studieplan[semester_index])

    if total_studiepoeng + emne.studiepoeng > 30:
        print(f"Feil: for mye studiepoeng i semester {semester}. Total: {total_studiepoeng}/30 poeng.")
        return True
    return False





def legg_til_emne_i_studieplan(emne, semester):
    semester_index = semester - 1

    # Не дублировать один и тот же предмет
    for sem in studieplan:
        if emne in sem:
            print(f"Feil: emne {emne.kode} er allerede i studieplanen.")
            return True

    # Проверка на правильный семестр
    if emne.semester == 'H' and semester not in [1, 3, 5]:
        print(f"Feil: høstemne {emne.kode} kan bare legges til i 1, 3 og 5 semester.")
        return True
    elif emne.semester == 'V' and semester not in [2, 4, 6]:
        print(f"Feil: våremne {emne.kode} kan legges bare i 2, 4 og 6 semester.")
        return True


    studieplan[semester_index].append(emne)
    print(f"Emne {emne.kode} lagt til i semester {semester}.")
    return False




def vis_emner():
    for i, emne in enumerate(emner):
        print(f"{i}: {emne.kode} - {emne.navn} ({emne.semester}), {emne.studiepoeng} sp")




def vis_studieplan():
    print("\nStudieplan:")

    for i, sem in enumerate(studieplan, start=1):
        if sem:
            print(f"\nSemester {i}:")
            total_studiepoenger = sum(e.studiepoeng for e in sem)
            for e in sem:
                print(f" - {e.kode} ({e.semester}, {e.studiepoeng} studiepoenger)")
            print(f"Total: {total_studiepoenger} studiepoeng")
        else:
            print(f"\nSemester {i}: ingen emner")