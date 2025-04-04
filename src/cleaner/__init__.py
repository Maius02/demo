
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

