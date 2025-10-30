class Emne:
    def __init__(self, kode, navn, semester, studiepoeng):
        self.kode = kode
        self.navn = navn
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f'{self.emnekode} ({self.navn}), {self.studiepoeng} studeipoeng'        