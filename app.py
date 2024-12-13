from flask import Flask
from routes.weather import weather_bp
from routes.calendar import calendar_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(weather_bp)
app.register_blueprint(calendar_bp)

if __name__ == '__main__':
    app.run(debug=True)