osoba1 = {
    "name": "Przemysław",
    "surname": "Polański",
    "city": "Warszawa",
    "hobby": ["Gitara", "Szachy", "Morze"]
}

osoba2 = {
    "name": "Anna",
    "surname": "Olenczyńska",
    "city": "Poznań",
    "hobby": ["Gotowanie", "Szydełkowanie", "Spacery"]
}

osoba3 = {
    "name": "Agata",
    "surname": "Woźniak",
    "city": "Gdańsk",
    "hobby": ["narciarstwo", "garncarstwo", "skoki"]
}

osoby = [osoba1, osoba2, osoba3]

print(osoby[2]["hobby"][1])
print(osoba3["hobby"][2])
print(osoba1)
print(osoba1["surname"])
print(osoba1["city"])
print(osoba2["surname"])
print(osoba2["city"])
print(osoba1["hobby"])
print(osoba1["hobby"][1])