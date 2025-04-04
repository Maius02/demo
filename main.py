#este programa limpia el dataset de espacios, cosas mal escritas y demas
#el objetivo es que los datos esten uniformes

dataset = [
    {
        "name": "Ana Torres      ", 
        "age": "28", 
        "gmail": "ana.torres@gmail.com", 
        "country": "Argentina"
    },
    {
        "name": "Lucas Pérez", 
        "age": "34",
        "gmail": "lucas.perezgmail.com", 
        "country": "España"
    },
    {
        "name": "Sofía Gómez", 
        "age": "cuarenta", 
        "gmail": "sofia.gomez@gmail.com", 
        "country": "México"
    },
    {
        "name": "Martín Silva", 
        "age": "N/A", 
        "gmail": "martin.sil", 
        "country": "Uruguay"
    },
    {
        "name": None, 
        "age": "25", 
        "gmail": None, 
        "country": "Chile"
    },
    {
        "name": "Diego Ramírez", 
        "age": "40", 
        "gmail": "diego.ramirez@gmail.com", 
        "country": "Colombia"
    },
]

#from cleaner import clean_data
from src import clean_data

print(clean_data(dataset))


