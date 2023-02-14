from deep_translator import GoogleTranslator
from readchar import readchar

lang = input("What language do you want to translate your text into\n"
             "(type it with 2 symbols like uk, en, es...):")
translator = GoogleTranslator(source='auto', target=lang)

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # get text from the txt file
    charAmount = []
    for x in lines:  # counts amount of symbols per line
        charAmount.append(len(x))
    lines = " ".join(lines).split(" ")

open("text.txt", "w").close()  # clear the txt file

with open("text.txt", "w", encoding="utf-8") as file:
    print("Started translating!")
    num = 0  # line number
    chars = 0  # chars in the line
    for x in lines:
        file.write(translator.translate(x) + " ")  # translate itself
        chars += len(x + " ")
        if chars >= charAmount[num - 1]:
            chars = 0
            num += 1  # goes to the next line
            file.write("\n")
print("Translated")
print("Press Any Key To Exit...")
k = readchar()