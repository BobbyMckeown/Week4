def CelToFar():
    Cel = CelTemp[:-1]
    Fahrenheit = (int(Cel) * 9 / 5) + 32
    return Fahrenheit


CelTemp = input("Please enter the temp in C: ")
print(CelToFar(), "f")
