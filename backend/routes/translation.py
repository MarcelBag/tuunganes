import requests

DEEPSEEK_API_KEY = 'sk-fabfe8a0a75a471c87da675679c66ee2'
DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/translate'

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