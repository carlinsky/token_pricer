# __init__.py
from model import Models
from openai_calculator import OpenAICostCalculator

def calculate_input_cost(model_name, filename):
    # Instantiate the Models class
    models = Models()
    if model_name in models.names():
        print ("model exists continue")
    else:
        print ("model doesnt exist")
        return

    try:
        with open(filename, 'r') as file:
            user_input = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None