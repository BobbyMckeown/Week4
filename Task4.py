def RemoveLast():
    if len(text) > 1:
        return text[:-1]  # [:-1] removes the last character in the string
    elif len(text) <= 1:
        return text


text = input("Please enter some text!: ")
print(RemoveLast())
