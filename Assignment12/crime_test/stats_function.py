import pandas as pd

def calculate_mean_median(data):
    if 'Vict age' not in data.columns:
        raise ValueError("No Vict age column in dataset")
    # We can always calculate the mean or median with missing value
    # But we need to make sure if Vict age column is entirely empty or not 
    if data['Vict age'].isnull().all():
        raise ValueError("Vict age column is empty")
    
    # Calculate mean and median 
    # Call name = data['name_of_the_column'].mean()/median()

    mean_age = data['Vict age'].mean()
    median_age = data['Vict age'].median()

    return mean_age, median_age

