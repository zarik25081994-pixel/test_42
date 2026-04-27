class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def info(self):
        return f'{self.day} {self.month} {self.year}'

    def get_ini(self):
        return self.year

d = date(26, 4, 2026)
print(d.info())
