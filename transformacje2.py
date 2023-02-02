import random as r

# lp1 = input("Podaj pierwszą liczbę: ")
# lp2 = input("Podaj drugą liczbę: ")
# print(int(lp1)+int(lp2))

# wpis = input("Podaj swoje imię: ")
# print("Twoje imię to: " + wpis)
wpis2 = input("Zgadnij liczbę od 0 do 10, którą za chwilę wyświetli komputer: ")
print("Wpisałeś liczbę: " + wpis2)
y = r.randint(1, 10)
#manipulacja kodem
if y < int(wpis2):
    y= r.randint(int(wpis2),10)
print("Komputer wylosował liczbę: " + str(y))
if int(wpis2) == y:
    print("Trafiłeś, brawo!")
else:
    print("Niestety, nie trafiłeś, spróbuj jeszcze raz!")