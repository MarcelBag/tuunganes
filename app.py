from flask import Flask, render_template
from backend.models.database import db, init_db
from backend.routes.subscription import subscription_bp

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

if __name__ == '__main__':
    app.run(debug=True)
