def CelToFar():
    Fahrenheit = (CelTemp * 9 / 5) + 32
    return Fahrenheit


def FarToCel():
    Celsius = (FarTemp - 32) * 5 / 9
    return Celsius


CelTemp = int(input("Please enter the temperature in C: "))
print(CelToFar())

FarTemp = int(input("Please enter the temperature in F: "))
print(FarToCel())
