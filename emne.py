class Emne:
    def __init__(self, emnekode, navn, tid, studiepoeng):
        self.emnekode = emnekode
        self.navn = navn
        self.tid = tid
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f'{self.emnekode} ({self.navn}), {self.studiepoeng} studeipoeng'        