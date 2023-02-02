owoce = ["jabłko", "gruszka", "śliwka"]
print("Lista to typ danych: " + str(type(owoce)))

owoce.insert(2, "arbuz")
owoce.append("mango")
owoce.append("dynia")


for x in owoce:
    print(x)

# [print(x) for x in owoce]



# for y in range(len(owoce)):
#     print(owoce[y])

# nowyOwoc = input("Dodaj owoc do listy:")
# owoce.append(nowyOwoc)
# print(owoce)

