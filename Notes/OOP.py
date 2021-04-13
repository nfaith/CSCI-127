
# r = Rectangle(Point(4, 5), 6, 5)




class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

class Game:

    def __init__(self,name_1, score_1, name_2, score_2, date):
        self.name_1 = name_1
        self.score_1 = score_1
        self.name_2 = name_2
        self.score_2 = score_2
        

# -----------------------------------------------------------

championship = Game("Montana State", 62, "Idaho State", 56, Date(3, 11, 2017))
print(championship)

ncaa = Game("Montana State", 63, "Washington", 91, Date(3, 18, 2018))
print(ncaa)
