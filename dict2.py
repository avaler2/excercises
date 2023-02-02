osoby = [
    {"name": "Marek",
    "email": "marek@marek.pl"},
    {"name": "Agata",
    "email": "agata@agata.pl"},
    {"name": "Jarosław",
    "email": "jaroslaw@jaroslaw.pl"}
]

print(osoby)
print(osoby[0])
print(osoby[0]["email"])

file = open("osoby.txt", "a", encoding="utf-8")
personName = input("Podaj swoje imię: ")
file.write("{\n")
file.write("\"name\":")
file.write("\"" + personName + "\"")
file.write(",\n")
personEmail = input("Podaj swojego emaila: ")
file.write("\"email\":")
file.write("\"" + personEmail + "\"")
file.write("\n},")
file.close()