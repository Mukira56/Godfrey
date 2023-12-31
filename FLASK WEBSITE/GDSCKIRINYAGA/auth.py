from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.quuery.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!', category='success')
            
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email doesn\'t exist.', category='error')
    return render_template("login.html", boolean=True)


@auth.route('/contact')
def logout():
    data = request.form
    print(data)
    return render_template("contact.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists.', category='error')
        elif len(first_name) < 3:
            flash('First name must be longer than 3 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 4 characters.', category='error')
        elif password1 != password2:
            flash("Your passwords doesn't match!", category='error')
        elif len(password1) < 8:
            flash('Your password  must not contain less than 8 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")
