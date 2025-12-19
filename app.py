# app.py
# flask --app app run --debug
################################################################################
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_assets import Environment, Bundle
from datetime import datetime
################################################################################
# My App + DB
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_smash.sqlite"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Task {self.id}"
################################################################################
# Assets
assets = Environment(app)

css = Bundle(
    'style.scss',
    filters='libsass',
    output='styles.css',
    depends='*.scss',
)

assets.register('asset_css', css)

print(app.static_folder)
################################################################################
#Homepage
@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        current_task = request.form['content']
        print(current_task)
        new_task = MyTask(content=current_task)
        try:
            print("trying to connect to DB....")
            print(new_task)
            print("DEBUG new_task:", new_task, "type:", type(new_task))
            db.session.add(new_task)
            db.session.commit()
            print("DEBUG new_task:", new_task, "type:", type(new_task))
            print("committed")
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return f"ERROR: {e}"
        
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)

# Delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"

# Update an Item
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template("update.html", task=task)




################################################################################
# load the app

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

