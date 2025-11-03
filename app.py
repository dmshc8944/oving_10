from data import emner, studieplaner, filnavn
from nytt_emne import lag_nytt_emne
from studieplan import Studieplan
from leselagre import lagre_alle_data, les_alle_data

def velg_studieplan():
    """Вспомогательная функция для выбора учебного плана"""
    if not studieplaner:
        print("Ingen studieplaner er opprettet ennå.")
        return None
    
    print("\nTilgjengelige studieplaner:")
    for i, plan in enumerate(studieplaner, 1):
        print(f"{i}. {plan.tittel} (ID: {plan.id})")
    
    try:
        valg = int(input("Velg studieplan (nummer): ")) - 1
        if 0 <= valg < len(studieplaner):
            return studieplaner[valg]
        else:
            print("Ugyldig valg.")
            return None
    except ValueError:
        print("Vennligst skriv inn et tall.")
        return None

def legg_til_emne_i_studieplan():
    """2. Добавить предмет в учебный план"""
    if not emner:
        print("Ingen emner er registrert ennå.")
        return
    
    plan = velg_studieplan()
    if not plan:
        return
    
    # Показываем все доступные предметы
    print("Tilgjengelige emner:")
    for i, emne in enumerate(emner, 1):
        print(f"{i}. {emne.kode} - {emne.navn} ({emne.semester}, {emne.studiepoeng}sp)")
    
    try:
        valg = int(input("Velg emne (nummer): ")) - 1
        if 0 <= valg < len(emner):
            valgt_emne = emner[valg]
            plan.legg_til_emne(valgt_emne)
            print(f"Emne {valgt_emne.kode} lagt til i studieplanen '{plan.tittel}'.")
        else:
            print("Ugyldig valg.")
    except ValueError:
        print("Vennligst skriv inn et tall.")

def fjern_emne_fra_studieplan():
    """3. Удалить предмет из учебного плана"""
    plan = velg_studieplan()
    if not plan:
        return
    
    if not any(plan.semestre):
        print("Denne studieplanen er tom.")
        return
    
    # Показываем все предметы в выбранном плане
    print(f"Emner i studieplanen '{plan.tittel}':")
    emne_liste = []
    for semester_num, semester_emner in enumerate(plan.semestre, 1):
        for emne in semester_emner:
            print(f"Semester {semester_num}: {emne.kode} - {emne.navn}")
            emne_liste.append((semester_num, emne))
    
    if not emne_liste:
        print("Ingen emner å fjerne.")
        return
    
    emnekode = input("Skriv inn emnekode du vil fjerne: ").upper()
    
    # Ищем и удаляем предмет
    fjernet = False
    for semester_num, semester_emner in enumerate(plan.semestre):
        for emne in semester_emner[:]:  # Копия списка для безопасного удаления
            if emne.kode == emnekode:
                plan.semestre[semester_num].remove(emne)
                print(f"Emne {emnekode} fjernet fra semester {semester_num + 1}.")
                fjernet = True
    
    if not fjernet:
        print(f"Fant ikke emne med kode {emnekode} i denne studieplanen.")

def skriv_ut_alle_emner():
    """4. Вывести список всех предметов"""
    if not emner:
        print("Ingen emner er registrert ennå.")
        return
    
    print("\n=== Alle registrerte emner ===")
    for i, emne in enumerate(emner, 1):
        print(f"{i}. {emne.kode} - {emne.navn} ({emne.semester}, {emne.studiepoeng} studiepoeng)")

def lag_ny_studieplan():
    """5. Создать новый пустой учебный план"""
    print("\n=== Lag ny studieplan ===")
    
    # Находим максимальный ID для создания нового
    max_id = max([plan.id for plan in studieplaner]) if studieplaner else 0
    ny_id = max_id + 1
    
    tittel = input("Skriv inn tittel for den nye studieplanen: ")
    
    if not tittel.strip():
        print("Tittel kan ikke være tom.")
        return
    
    # Создаем новый учебный план
    ny_plan = Studieplan(ny_id, tittel)
    studieplaner.append(ny_plan)
    
    print(f"Ny studieplan '{tittel}' (ID: {ny_id}) er opprettet.")

def skriv_ut_studieplan():
    """6. Вывести учебный план с предметами по семестрам"""
    plan = velg_studieplan()
    if not plan:
        return
    
    print(f"\n=== Studieplan: {plan.tittel} (ID: {plan.id}) ===")
    
    tom_plan = True
    for semester_num, semester_emner in enumerate(plan.semestre, 1):
        print(f"\nSemester {semester_num}:")
        if semester_emner:
            for emne in semester_emner:
                print(f"  - {emne.kode}: {emne.navn} ({emne.studiepoeng}sp)")
            tom_plan = False
        else:
            print("  (ingen emner)")
    
    if tom_plan:
        print("Denne studieplanen er tom.")

def sjekk_studieplan_gyldig():
    """7. Проверить валидность учебного плана"""
    plan = velg_studieplan()
    if not plan:
        return
    
    print(f"\n=== Sjekker gyldighet for: {plan.tittel} ===")
    
    # Проверяем семестры предметов
    problemer = []
    for semester_num, semester_emner in enumerate(plan.semestre, 1):
        for emne in semester_emner:
            # Проверяем, что предмет в правильном семестре (H=1,3,5; V=2,4,6)
            if emne.semester == 'H' and semester_num % 2 == 0:
                problemer.append(f"Hostemne {emne.kode} i vårsemester {semester_num}")
            elif emne.semester == 'V' and semester_num % 2 == 1:
                problemer.append(f"Våremne {emne.kode} i høstsemester {semester_num}")
    
    if not problemer:
        print("✓ Studieplanen ser ut til å være gyldig.")
    else:
        print("✗ Problemer funnet:")
        for problem in problemer:
            print(f"  - {problem}")

def finn_studieplaner_med_emne():
    """8. Найти учебные планы, использующие указанный предмет"""
    if not emner:
        print("Ingen emner er registrert ennå.")
        return
    
    emnekode = input("Skriv inn emnekode: ").upper()
    
    # Проверяем, существует ли предмет
    emne_finnes = any(emne.kode == emnekode for emne in emner)
    if not emne_finnes:
        print(f"Emne med kode {emnekode} finnes ikke.")
        return
    
    # Ищем в каких планах используется предмет
    planer_med_emne = []
    for plan in studieplaner:
        for semester_emner in plan.semestre:
            for emne in semester_emner:
                if emne.kode == emnekode:
                    planer_med_emne.append(plan)
                    break
    
    if planer_med_emne:
        print(f"Emne {emnekode} brukes i følgende studieplaner:")
        for plan in planer_med_emne:
            print(f"  - {plan.tittel} (ID: {plan.id})")
    else:
        print(f"Emne {emnekode} brukes ikke i noen studieplaner.")

def hovedmeny():
    """Главное меню"""
    while True:
        print("\n" + "="*50)
        print("STUDIEPLAN-SYSTEM")
        print("="*50)
        print("1. Lag et nytt emne")
        print("2. Legg til et emne i en studieplan")
        print("3. Fjern et emne fra en studieplan")
        print("4. Skriv ut ei liste over alle registrerte emner")
        print("5. Lag en ny tom studieplan")
        print("6. Skriv ut en studieplan med hvilke emner som er i hvert semester")
        print("7. Sjekk om en studieplan er gyldig eller ikke")
        print("8. Finn hvilke studieplaner som bruker et oppgitt emne")
        print("9. Lagre emnene og studieplanene til fil")
        print("10. Les inn emnene og studieplanene fra fil")
        print("11. Avslutt")
        print("="*50)
        
        valg = input("Velg et alternativ (1-11): ")
        
        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            legg_til_emne_i_studieplan()
        elif valg == "3":
            fjern_emne_fra_studieplan()
        elif valg == "4":
            skriv_ut_alle_emner()
        elif valg == "5":
            lag_ny_studieplan()
        elif valg == "6":
            skriv_ut_studieplan()
        elif valg == "7":
            sjekk_studieplan_gyldig()
        elif valg == "8":
            finn_studieplaner_med_emne()
        elif valg == "9":
            lagre_alle_data(emner, studieplaner, filnavn)
        elif valg == "10":
            les_alle_data(emner, studieplaner, filnavn)
        elif valg == "11":
            print("Avslutter programmet. Ha det bra!")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    hovedmeny()