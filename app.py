from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

# My App

app = Flask(__name__)
assets = Environment(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_smash.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

css = Bundle(
    'style.scss',
    filters='libsass',
    output='styles.css',
    depends='*.scss',
)

assets.register('asset_css', css)

print(app.static_folder)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

