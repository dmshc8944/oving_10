class Studieplan:
    def __init__(self, id, tittel):
        self.id = id
        self.tittel = tittel
        self.semestre = [[] for _ in range(6)]  # по одному списку на каждый семестр

    def legg_til_emne(self, emne):
        """Добавить предмет в нужный семестр"""
        self.semestre[emne.semester - 1].append(emne)
