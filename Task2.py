def UpperAndLower():
    uppercase = 0
    lowercase = 0
    for character in text:  # Checking in letter in the string
        if character.islower():
            lowercase += 1  # When a letter is lowercase the counter increases
        elif character.isupper():
            uppercase += 1  # When a letter is uppercase the counter also increments
    return uppercase, lowercase


text = input("Enter in a string: ")
print("upper , lower",
      UpperAndLower())
