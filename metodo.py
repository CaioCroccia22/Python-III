class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("#Dados do filme")
        print(f"Nome do filme: {self.name}")