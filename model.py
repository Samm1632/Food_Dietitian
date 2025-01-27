from langchain_openai.chat_models import ChatOpenAI

def generate_recipe_insight(recipe_name):
    model = ChatOpenAI(temperature=0.4, api_key="user-api-key")
    prompt = f"Provide more details about the recipe '{recipe_name}', including variations and cooking tips."
    response = model.invoke(prompt)
    return response