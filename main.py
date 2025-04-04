#este programa limpia el dataset de espacios, cosas mal escritas y demas
#el objetivo es que los datos esten uniformes

def clean_name(name):
    """Si el nombre tiene valor, limpia los espacios en blanco    """
    return name.strip().capitalize() if name else None

def clean_age(age):
    """si la edad tiene un valor, devuelve la edad en entero"""
    if not age or age.lower() in ["n/a","null","name",""]:
        return None
    
    if age.isnumeric():
        return int(age)
    else:
        return None

def clean_gmail(gmail):
    """si el email tiene valor, lo devuelve en minuscula, ademas debe tener el arroba"""
    if gmail is None:
        return None

    gmail = gmail.lower().strip()
    return gmail if "@" in gmail else None

def clean_country(country):
    """si el pais tiene valor, lo devuelve en mayuscula""" 
    if country is None:
        return None
    
    clean_country = country.strip().capitalize()
    return clean_country if clean_country in ["Argentina","Brasil","Chile"] else "Resto del mundo"

def clean_data(dataset):
    """Limpia los datos del dataset"""
    for data in dataset:
        data["name"] = clean_name(data["name"])
        data["age"] = clean_age(data["age"])
        data["gmail"] = clean_gmail(data["gmail"])
        data["country"] = clean_country(data["country"])
    return dataset


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

#EJECUCION DEL PROGRAMA
print(clean_data(dataset))


