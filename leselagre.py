def lagre_alle_data(emner, studieplaner, filnavn):
    """9. Сохранить все данные в файл"""
    try:
        with open(filnavn, "w", encoding="utf-8") as f:
            # Сохраняем предметы
            f.write("=== Emner ===\n")
            for emne in emner:
                f.write(f"{emne.kode};{emne.navn};{emne.semester};{emne.studiepoeng}\n")
            
            # Сохраняем учебные планы
            f.write("\n=== Studieplaner ===\n")
            for plan in studieplaner:
                f.write(f"Plan;{plan.id};{plan.tittel}\n")
                for semester_num, semester_emner in enumerate(plan.semestre, 1):
                    emne_koder = [emne.kode for emne in semester_emner]
                    if emne_koder:  # Сохраняем только непустые семестры
                        f.write(f"Semester{semester_num};{','.join(emne_koder)}\n")
        
        print(f"Alle data er lagret til '{filnavn}'.")
        print(f"Lagret {len(emner)} emner og {len(studieplaner)} studieplaner.")
    
    except Exception as e:
        print(f"Feil ved lagring: {e}")

def les_alle_data(emner, studieplaner, filnavn):
    """10. Загрузить все данные из файла"""
    try:
        with open(filnavn, "r", encoding="utf-8") as f:
            linjer = f.readlines()
        
        # Очищаем текущие данные
        emner.clear()
        studieplaner.clear()
        
        seksjon = None
        current_plan = None
        
        for linje in linjer:
            linje = linje.strip()
            if not linje:
                continue
            
            if linje == "=== Emner ===":
                seksjon = "emner"
            elif linje == "=== Studieplaner ===":
                seksjon = "studieplaner"
            elif seksjon == "emner" and ";" in linje:
                # Формат: KODE;NAVN;SEMESTER;STUDIEPOENG
                deler = linje.split(";")
                if len(deler) == 4:
                    kode, navn, semester, studiepoeng = deler
                    from emne import Emne
                    nytt_emne = Emne(kode, navn, semester, int(studiepoeng))
                    emner.append(nytt_emne)
            
            elif seksjon == "studieplaner":
                if linje.startswith("Plan;") and ";" in linje:
                    # Формат: Plan;ID;TITTEL
                    deler = linje.split(";")
                    if len(deler) >= 3:
                        plan_id = int(deler[1])
                        plan_tittel = deler[2]
                        from studieplan import Studieplan
                        current_plan = Studieplan(plan_id, plan_tittel)
                        studieplaner.append(current_plan)
                
                elif linje.startswith("Semester") and ";" in linje and current_plan:
                    # Формат: SemesterX;KODE1,KODE2,...
                    deler = linje.split(";")
                    if len(deler) == 2:
                        semester_num = int(deler[0].replace("Semester", ""))
                        emne_koder = deler[1].split(",") if deler[1] else []
                        
                        # Добавляем предметы в семестр
                        for kode in emne_koder:
                            if kode:  # Проверяем, что код не пустой
                                # Находим объект предмета по коду
                                for emne in emner:
                                    if emne.kode == kode:
                                        current_plan.semestre[semester_num - 1].append(emne)
                                        break
        
        print(f"Data er lest inn fra '{filnavn}'.")
        print(f"Lest inn {len(emner)} emner og {len(studieplaner)} studieplaner.")
    
    except FileNotFoundError:
        print(f"Fil '{filnavn}' ikke funnet.")
    except Exception as e:
        print(f"Feil ved innlesing: {e}")