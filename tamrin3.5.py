class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y, "-", self.m, "-", self.d)

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
        result.y= d2.y- self.y
        result.m= d2.m- self.m
        result.d= d2.d- self.d
        if result.d < 0:
            result.d += 30
            result.m -= 1
        if result.m < 12:
            result.m += 12
            result.y -= 1

        return result

    def month_name (self):
        
        if self.m == 1: 
            month="Farvardin🌼🌼"
        elif self.m == 2:
            month = "Ordibehesht🌺"
        elif self.m == 3:
            month ="Khordad🍓🍓"
        elif self.m == 4:
            month = "Tir🍇"
        elif self.m == 5:
            month = "Mordad🔅"
        elif self.m == 6:
            month = "Shahrivar💖"
        elif self.m == 7:
            month = "Mehr🏵🏵"
        elif self.m == 8:
            month = "Aban🍂"
        elif self.m == 9:
            month = "Azar🍁🍁"            
        elif self.m == 10:
            month = "Dey"
        elif self.m == 11:
            month = "Bahman🎂🎂"
        elif self.m == 12:
            month = "Esfand😍😍"           
        return month

    def Valid_Date (self):
        
        if self.d < 1 or self.d > 31: 

            day=("False Day")
            return day
        if self.m < 1 or self.m > 12: 

            month=("False month")
            return month
        if self.y < 1 : 

            year=("False Year")
            return year
        
calender1 = Date(1360,11,25)
calender2 = Date(1400,10,20)

print("first date : ")
calender1.show()

print("second date :")
calender2.show()

s = calender1.sum(calender2)
print("Sum of 2 dates : ")
s.show()

Subtraction = calender1.sub(calender2)
print("Subtraction of 2 dates  : ")
Subtraction.show()

Month_Name = calender2.month_name()
print("Month name ", Month_Name)

Valid_date = calender1.Valid_Date()
print("False calender1:",   Valid_date)

Valid_date = calender2.Valid_Date()
print("False calender2:",   Valid_date)
