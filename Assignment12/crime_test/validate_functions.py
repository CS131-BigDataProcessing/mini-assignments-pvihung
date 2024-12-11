def validate_vict_sex(data):
    # this is used for checking if this column exist or not
    if 'Vict sex' not in data.columns:
        raise ValueError("No Vict sex column in the dataset")

    # in/not in to check if the value you want to use fit in the required set or no 
    for value in data['Vict sex']:
        if value not in ['M','F']: 
            return False
    return True

def validate_vict_age(data):
    if 'Vict age' not in data.columns:
        raise ValueError("No Vict age column in the dataset")

    for value in data['Vict age']:
        # In python, you cant use ||, you must use or 
        # None also used in Python
        if value is None or not (1 <= value <= 100):
            return False
        return True
        

