from flask import Flask, render_template, request
from backend.models.database import db, init_db
from backend.routes.subscription import subscription_bp
from dotenv import load_dotenv  # dotenv to load env variables
import os  # Import os to access env variables

# Load env variables from .env file
load_dotenv()

app = Flask(
    __name__,
    template_folder='backend/templates',  # Path to templates
    static_folder='static'  # Path to static files
)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tuunganes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)

# Register the Blueprint
app.register_blueprint(subscription_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/actions/computer')
def computer():
    return render_template('IT.html')

@app.route('/actions/computer/learn-more')
def computer_learn_more():
    return render_template('learnmoreit.html')

@app.route('/actions/agriculture')
def agriculture():
    return render_template('agriculture.html')

@app.route('/actions/agriculture/learn-more')
def agriculture_learn_more():  # Renamed this function to avoid the conflict
    return render_template('learnmoreagri.html')

@app.route('/actions')
def actions():
    return render_template('actions.html')

# Add a before_request handler to detect the user's language
@app.before_request
def before_request():
    # Detect user's language from the request headers
    user_language = request.accept_languages.best_match(['en', 'fr', 'de'])  # Add more languages as needed
    if not user_language:
        user_language = 'en'  # Default to English if no language is detected

    # Store the user's language in the request context
    request.user_language = user_language

# Function to translate content (if needed)
def translate_content(content, target_language):
    # You can integrate the translation logic here if needed
    # For now, this is a placeholder
    return content

if __name__ == '__main__':
    # Load the Deepseek API key and URL from environment variables
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL')

    # Verify that the API key and URL are loaded
    if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
        print("Error: DEEPSEEK_API_KEY or DEEPSEEK_API_URL not found in environment variables.")
    else:
        print("Deepseek API key and URL loaded successfully.")

    # Run the Flask app
    app.run(debug=False)