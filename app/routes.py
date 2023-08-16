from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
import os
import string
import random
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Image
from app import db
from app.forms import Login, Register
from config import upload_folder


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    user_id = current_user.get_id()
    image_files = Image.query.filter_by(user_id=user_id).all()

    return render_template('home.html', title='Home', images=image_files)


@app.route('/delete/<filename>')
def delete_image(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Image deleted successfully', 'success')
    return redirect(url_for('index'))


@app.route("/addImage", methods=["POST"])
def addImage():
    if request.method == "POST":
        file = request.files['img']
        filename = generate_random_string(20)

        ext = os.path.splitext(file.filename)[1] 
        filename_with_extension = filename + ext

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'], filename_with_extension)
        file.save(filepath)

        user_id = current_user.get_id()
        image = Image(user_id=user_id, path=filename_with_extension)
        db.session.add(image)
        db.session.commit()

        flash('Image uploaded successfully', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_image.html', title='Add Image')


@app.route("/", methods=["GET", "POST"])
def main():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))

        flash("Invalid username or password", "danger")
        return redirect(url_for("login"))

    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = Register()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            flash("Username already exists", "danger")
            return redirect(url_for("login"))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful", "success")
        return redirect(url_for("login"))

    return render_template("register.html", title="Register", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
