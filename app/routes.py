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


@app.get('/home')
@login_required
def index():
    user_id = current_user.get_id()
    image_files = Image.query.filter_by(user_id=user_id).all()

    return render_template('home.html', title='Home', images=image_files, active='home')


@app.route('/delete/<filename>')
@login_required
def delete_image(filename):
    image = Image.query.filter_by(path=filename).first()
    db.session.delete(image)
    db.session.commit()
    
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Image deleted successfully', 'success')
    return redirect(url_for('index'))


@app.route("/addImage", methods=["GET", "POST"])
@login_required
def addImage():
    if request.method == "POST":
        file = request.files['img']
        title = request.form['title']
        description = request.form['description']

        if file.filename == '' or file.filename.split('.')[-1] not in app.config['UPLOAD_EXTENSIONS']:
            flash('No image selected for uploading', 'danger')
            return redirect(url_for('index'))
        
        filename = generate_random_string(20)

        ext = os.path.splitext(file.filename)[1] 
        filename_with_extension = filename + ext

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'], filename_with_extension)
        file.save(filepath)

        user_id = current_user.get_id()
        image = Image(user_id=user_id, path=filename_with_extension, title=title, content=description)
        db.session.add(image)
        db.session.commit()

        flash('Image uploaded successfully', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_image.html', title='Add Image', active='addImage')


@app.route("/image/<image_id>", methods=["GET"])
def singleImage(image_id):
    image = Image.query.filter_by(id=image_id).first()
    return render_template("single_image.html", title="Image", image=image)


@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html", title="Settings", active="settings")

@app.route("/")
def main():
    return redirect(url_for("login"))

@app.route("/deleteAll", methods=["GET"])
def deleteAll():
    user_id = current_user.get_id()
    image_files = Image.query.filter_by(user_id=user_id).all()

    for image in image_files:
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], image.path)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image.path))

        db.session.delete(image)
        db.session.commit()

    flash("All images deleted successfully", "success")
    return redirect(url_for("index"))

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

@app.route("/deleteAccount", methods=["POST"])
def deleteAccount():
    flash("Account deleted successfully", "success")
    return redirect(url_for("login"))
