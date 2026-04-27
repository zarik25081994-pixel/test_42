class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def info(self):
        return f'{self.day} {self.month} {self.year}'

    def get_ini(self):
        return self.year

    def hiot_frs(self):
        return self.day
    
    def hop_steo(self):
        return self.month
        
d = date(26, 4, 2026)
print(d.info())
