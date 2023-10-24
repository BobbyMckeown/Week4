# Task 1
def VerifyInput():
    if 0 < EnterNumber < 101:
        return "True"
    else:
        return "False"


EnterNumber = int(input("Please enter a random number: "))
print(VerifyInput())



