from statistics import mean


def CelToFar():
    Cel = TempInC[:-1]
    Fahrenheit = (int(Cel) * 9 / 5) + 32
    Fahrenheit = str(Fahrenheit) + "F"
    return Fahrenheit


Temps = []
TakenTemp = 0
while TakenTemp != 6:
    TempInC = input("Enter the temp in C")
    if len(TempInC) > 1:
        Temps.append(CelToFar())
        TakenTemp += 1
    else:
        print("Wrong format! Try again")
        break

print(Temps)
