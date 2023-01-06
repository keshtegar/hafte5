class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d


    def show(self):
        print(self.y, "_", self.m, "_", self.d)


    def sum(self, d2):
        result = Date(None, None, None)
        result.y = self.y + d2.y
        result.m = self.m + d2.m
        result.d = self.d + d2.d

        if result.d >= 30:
            result.d -= 30
            result.m += 1

        if result.m >= 12:
            result.m -= 12
            result.y += 1

        return result


    def sub(self, d2):
        result = Date(None, None, None)
        result.y = self.y - d2.y
        result.m = self.m - d2.m
        result.d = self.d - d2.d

        if result.d < 0:
            result.d += 30
            result.m -= 1

        if result.m < 12:
            result.m += 12
            result.y -= 1

        return result



    def GetMonthName (self):
        
        if self.m == 1: 

            month="farvardin 🌸🌸🌸"

        elif self.m == 2:
            month = "ordibehesht 🌼🌷🌺"
        elif self.m == 3:
            month ="khordad 🍋🍓"

        elif self.m == 4:
            month = "🍦🍧"

        elif self.m == 5:
            month = "Mordad🥂🥤"

        elif self.m == 6:
            month = "Shahrivar🍒🍇🍇"

        elif self.m == 7:
            month = "Mehr🌿"

        elif self.m == 8:
            month = "Aban🍁🍁"

        elif self.m == 9:
            month = "Azar🍂 "            

        elif self.m == 10:
            month = "Dey💗💓"

        elif self.m == 11:
            month = "Bahman🎂🎂"

        elif self.m == 12:
            month = "Esfand🙌"           

        return month

             
calender1 = Date(1401, 2, 12)
calender2 = Date(1354, 12, 10)

print("calender is: ")
calender1.show()

print("calender2 is: ")
calender2.show()

s = calender1.sum(calender2)
print("calender1 + calender2 = : ")
s.show()

m = calender1.sub(calender2)
print("calender1 - calender2 = : ")
m.show()

MonthName = calender1.GetMonthName()
print("month of calender is:\n", MonthName)