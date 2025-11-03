class Studieplan:
    def __init__(self, id, tittel):
        self.id = id
        self.tittel = tittel
        self.semestre = [[] for _ in range(6)]  # 6 семестров

    def legg_til_emne(self, emne):
        """Добавить предмет в учебный план"""
        # Определяем номер семестра на основе типа семестра (H/V)
        # H (осень) = 1, 3, 5 семестры
        # V (весна) = 2, 4, 6 семестры
        
        print(f"\nVelg semester for {emne.kode} ({emne.navn}):")
        if emne.semester == 'H':
            print("Gyldige høstsemestre: 1, 3, 5")
            semestre_valg = ['1', '3', '5']
        else:  # V
            print("Gyldige vårsemestre: 2, 4, 6")
            semestre_valg = ['2', '4', '6']
        
        valgt_semester = input("Skriv inn semester (1-6): ")
        
        if valgt_semester in semestre_valg:
            semester_index = int(valgt_semester) - 1
            self.semestre[semester_index].append(emne)
            print(f"Emne {emne.kode} lagt til i semester {valgt_semester}.")
        else:
            print(f"Ugyldig semester for {emne.semester}-emne. Må være {', '.join(semestre_valg)}")

    def __str__(self):
        """Строковое представление учебного плана"""
        result = f"Studieplan: {self.tittel} (ID: {self.id})\n"
        for i, semester in enumerate(self.semestre, 1):
            result += f"Semester {i}: "
            if semester:
                emne_koder = [emne.kode for emne in semester]
                result += ", ".join(emne_koder)
            else:
                result += "Ingen emner"
            result += "\n"
        return result