def calculate_calories(height, weight, age, gender):
    """
    Calculate daily calorie intake based on Mifflin-St Jeor Equation.
    """
    if gender == "Male":
        calories = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        calories = 10 * weight + 6.25 * height - 5 * age - 161
    return round(calories)