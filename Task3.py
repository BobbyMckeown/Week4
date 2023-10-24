def CheckName():
    temp = name.strip(name[0]).lower()  # Makes all the characters lowercase and removes the first charter
    temp2 = name[0].upper()  # Takes the first letter and makes it uppercase
    newName = temp2 + temp   # Concatenates the two string to make the name
    return newName


name = input("Please enter your name: ")
print("Greetings,", CheckName(), "!")
