from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
import os
import string
import random

upload_folder = os.path.join(os.getcwd(), 'app', 'static', 'image')
app.config['UPLOAD_FOLDER'] = upload_folder

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files['img']
        filename = generate_random_string(10)
        ext = os.path.splitext(file.filename)[1]  # Dosya uzantısını al
        filename_with_extension = filename + ext  # Yeni dosya adını uzantıyla birleştir
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename_with_extension)
        file.save(filepath)
        flash('Image uploaded successfully', 'success')
        """ filename = secure_filename(file.filename)
        if filename in os.listdir(upload_folder):
            flash('Image already exists', 'danger')
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image uploaded successfully', 'success') """

        return redirect(url_for('index'))

    image_files = os.listdir(upload_folder)
    return render_template('index.html', title='Home', images=image_files)


@app.route('/delete/<filename>')
def delete_image(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Image deleted successfully', 'success')
    return redirect(url_for('index'))
