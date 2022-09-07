from flask import render_template
from cooknride import app, db
from cooknride.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")