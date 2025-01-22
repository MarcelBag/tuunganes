from flask import Flask, render_template
from backend.routes.subscription import subscription_bp

app = Flask(
    __name__,
    template_folder='backend/templates',  # Path to templates
    static_folder='static'  # Path to static files
)

# Register the Blueprint
app.register_blueprint(subscription_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
