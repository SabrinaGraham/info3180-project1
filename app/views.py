"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from .forms import addNewPropertyForm
from app.models import Properties
import psycopg2

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Sabrina Graham")

@app.route('/properties/<filename>')
def get_image(filename):
    root_dir=os.getcwd()
    return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']), filename)

def get_uploaded_images():
    rootdir=os.getcwd()
    upload_path= rootdir + '/uploads'
    upload_lst=[]
    for subdir, dirs, files in os.walk(upload_path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')):
                upload_lst.append(file)
    return upload_lst

def get_property():
    p_lst=Properties.query.all()
    records=[{"id":p.id,
        "title":p.title,
        "location":p.location,
        "price":p.price,
        "bedroom":p.bedroom,
        "bathroom":p.bathroom,
        "propertyType":p.propertyType,
        "desc":p.description,"photo":p.photo_name} for p in p_lst]
    return records


@app.route('/properties/')
def properties():
    prop=get_property()
    return render_template('properties.html', file_list=prop)

@app.route('/properties/create/', methods=['POST','GET'])
def create_property():
    form = addNewPropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            img=form.photo.data
            print('photo filename', img)
            filename=secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            form_data=Properties()

            form_data.title=form.title.data
            form_data.description=form.description.data
            form_data.bedroom=form.bedroom.data
            form_data.bathroom=form.bathroom.data
            form_data.price=form.price.data
            form_data.location=form.location.data
            form_data.propertyType=form.propertyType.data
            form_data.photo_name=filename

            db.session.add(form_data)
            db.session.commit()

            flash ('Property sucessfully added!')
            return redirect(url_for('properties'))
    return render_template('create.html', form=form)

@app.route('/properties/<propertyid>/')
def view_property(propertyid):
    #this_property
    records=get_property()
    for r in records:
        print(r['id'],propertyid)
        if str(r['id'])==str(propertyid):
            print("pass")
            this_property=r
            print(this_property)
    return render_template('view_property.html', prop=this_property )
    #return send_form_directory(os.path.join(root_dir,app.config['PROPERTY_LIST']


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
