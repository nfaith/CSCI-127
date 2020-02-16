
# 1.)

score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0
for ch in score_differences:
    if score_differences.get(ch) < 0:
        losses += 1
    else:
        wins += 1
        


print(wins, "wins -", losses, "losses")



# 2.)

class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer


class Refrigerator(Appliance):

    def __init__(self, manufacturer, cooling_agent):
        Appliance.__init__(self,manufacturer)
        self.cooling_agent = cooling_agent

    def __str__(self):
        answer = "The " + self.manufacturer + " refrigerator contains refrigerant "+ self.cooling_agent
        return answer



my_refrigerator = Refrigerator("Samsung", "R134a") # R134a is the refrigerant (cooling agent) used
print(my_refrigerator)

