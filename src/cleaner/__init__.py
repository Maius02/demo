
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

#OTRA FORMA DE IMPORTAR, ES MEJOR YA Q SE DE DONDE LLAMO A LA FUNCION
'''
#en el caso que los tenga en otra carpeta
from src import cleaner

def clean_data(dataset):
    """Limpia los datos del dataset"""
    for data in dataset:
        data["name"] = cleaner.clean_name(data["name"])
        data["age"] = cleaner.clean_age(data["age"])
        data["gmail"] = cleaner.clean_gmail(data["gmail"])
        data["country"] = cleaner.clean_country(data["country"])
    return dataset
'''