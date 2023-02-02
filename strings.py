zdanie3 = """Witaj w świecie Pythona, 'Vikingów' i języków programowania!"""
zdanie = "Witaj w świecie Pythona, \"Vikingów\" i języków programowania!"
print(zdanie)
print("Długość zdania to: " + str(len(zdanie)) + " liter(y)!")
# for litera in zdanie:
#     if litera == " ":
#         print("Spacja")

# odp = input("Sprawdź czy istnieje dane słowo w zdaniu: ")
# print(odp not in zdanie)
print(zdanie.strip())
print(zdanie.replace("e", "eee"))
lst = zdanie.split(" ")
print(lst[-1])

# wiek = input("Podaj wiek swojego zwierzaka w domu: ")
# print("Wiek Twojego zwierzaka to: " + str(wiek))
# print("Wiek Twojego zwierzaka to {}".format(wiek))