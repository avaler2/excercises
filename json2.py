import json

daneJson = '{"name": "Przemysław", "fname": "Polański", "secret": 33}'

file= open("example_2.json", encoding="utf-8")
fileContents = file.read()
dane = json.loads(fileContents)
print(dane["quiz"]["maths"]["q1"]["question"])
file.close()

writeFile = open("newJson.json", "w", encoding="utf-8")
writeFile.write(json.dumps(daneJson, indent=4, separators=(". ", " = ")))
writeFile.close()
file = open("newJson.json", "r", encoding="utf-8")
print(file.read())
