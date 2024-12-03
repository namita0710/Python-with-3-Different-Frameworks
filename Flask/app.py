from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Home route - Read all Todo
@app.get("/")
def index():
    todos = db.session.query(Todo).all()
    return render_template("base.html", todos=todos)

@app.get("/home")
def home():
    todos = db.session.query(Todo).all()
    return render_template("base.html", todos=todos)

# Create a new Todo
@app.post("/add")
def add():
        title = request.form.get("title")
        complete = 0
        if not title:
            flash("Title is required!")
            return redirect(url_for("add"))
        
        new_Todo = Todo(title=title, complete=complete)
        db.session.add(new_Todo)
        db.session.commit()
        flash("Todo added successfully!")
        return redirect(url_for("home"))
  
# Update an existing Todo
@app.get("/update/<int:id>")
def update(id):
    todo = db.session.query(Todo).filter(Todo.id == id).first()
    if todo:
        todo.complete = not todo.complete
    db.session.commit()
    flash("Todo updated successfully!")
    return redirect(url_for("home"))
    
# Delete a Todo
@app.post("/delete/<int:id>")
def delete(id):
    todo = db.session.query(Todo).filter(Todo.id == id).first()
    db.session.delete(todo)
    db.session.commit()
    flash("Todo deleted successfully!")
    return redirect(url_for("home"))
