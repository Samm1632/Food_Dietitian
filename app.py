import streamlit as st
import pandas as pd
from calorie import calculate_calories
from model import generate_recipe_insight

# Initialize Streamlit
st.title("Calorie Intake and Recipe Recommendation")
recipes_data = pd.read_csv("data/All_Diets.csv")

# Streamlit form for user inputs
with st.form("calorie_form"):
    st.header("Enter Your Details")
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    age = st.number_input("Age (years)", min_value=10, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])

    submitted = st.form_submit_button("Submit")

    if submitted:
        # Calculate required calorie intake
        daily_calories = calculate_calories(height, weight, age, gender)
        st.success(f"Your recommended daily calorie intake is {daily_calories} kcal.")

        # Display detailed recipes
        st.header("Detailed Recipes")
        for _,recipe in recipes_data.iterrows():
            st.subheader(recipe["Recipe_name"])
            st.text(f"Protein: {recipe['Protein(g)']}g, Carbs: {recipe['Carbs(g)']}g, Fat: {recipe['Fat(g)']}g")
            # Use LLM to generate more detailed insights if necessary
            insights = generate_recipe_insight(recipe["Recipe_name"])
            st.info(insights)