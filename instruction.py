import ollama
import requests

def get_ollama_response(prompt):
    """
    Sends a prompt to the Ollama model and returns the response.

    Args:
        prompt (str): The input prompt for the model.
        model (str): The name of the model to use. Default is "default-model".
        api_url (str): The base URL of the Ollama API. Default is "http://localhost:8000/api".

    Returns:
        str: The response from the model.
    """
    client = ollama.Client()
    model = "genai2"

    try:
        response = client.generate(model=model, prompt=prompt)
        return response.response
    except requests.RequestException as e:
        return f"Error: {e}"