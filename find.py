cars = ["BMW", "Mercedes", "Audi", "Porsche", "Aston Martin"]
car = input("Jakiego samochodu szukasz?")
CARFOUND = False
for x in cars:
    if x == car:
        print("Yeah, " + car + " jest na liście!")
        CARFOUND = True
        break
if CARFOUND is False:
    print("No, niestety, nie ma " + car + " na tej liście!")