url = "https://api-colombia.com/api/v1/Department"
respuesta = requests.get(url)
datos = respuesta.json
for d in datos:
    print(d["name"]