import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key and URL from environment variables
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL')

def detect_language(text):
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text
    }
    response = requests.post(f'{DEEPSEEK_API_URL}/detect', headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('language')
    return None

def translate_text(text, target_language):
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'target_language': target_language
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('translated_text')
    return text  # Return original text if translation fails