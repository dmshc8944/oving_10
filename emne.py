class Emne:
    def __init__(self, kode, navn, semester, studiepoeng):
        self.kode = kode
        self.navn = navn
        self.semester = semester.upper()  # H или V
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f'{self.kode} ({self.navn}), {self.studiepoeng} studiepoeng'
    
    def __repr__(self):
        return f"Emne('{self.kode}', '{self.navn}', '{self.semester}', {self.studiepoeng})"