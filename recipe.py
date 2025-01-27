import pandas as pd

def recommend_recipes(data, calorie_range):
    """
    Recommend recipes based on calorie range from the dataset.
    """
    filtered_data = data[
        (data['Calories'] >= calorie_range[0]) & (data['Calories'] <= calorie_range[1])
    ]
    return filtered_data[['Recipe', 'Calories', 'Ingredients']]
