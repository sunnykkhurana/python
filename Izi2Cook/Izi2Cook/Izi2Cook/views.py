"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, url_for, redirect, request
from Izi2Cook import app
from Izi2Cook.modal.register import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,)


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,)


@app.route('/recipes')
def recipes():
    """Renders the recipes page."""
    return render_template('recipes.html',
        title='recipes',
        year=datetime.now().year,)


@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return('login.html')
    else:
        return render_template('register.html',
        title='register',
        year=datetime.now().year,
        )

@app.route('/login')
def login():
    
    return render_template('login.html',
        title='register',
        year=datetime.now().year,
        )
