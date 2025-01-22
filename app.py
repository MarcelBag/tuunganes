from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='backend/templates', #ttemplates path
    static_folder='static'  # static files
)

@app.route('/')
def home():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
