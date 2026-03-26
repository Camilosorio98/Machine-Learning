from flask import Flask
from app.controllers.ml_controller import ml_bp

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Registering the Blueprint
app.register_blueprint(ml_bp)

if __name__ == "__main__":
    app.run(debug=True)