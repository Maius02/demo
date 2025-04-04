
from src.cleaner import clean_name, clean_age, clean_gmail, clean_country

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