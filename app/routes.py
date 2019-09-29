from flask import render_template, flash, redirect
from app import app
from app.forms import UploadForm

@app.route('/')
@app.route('/index')
def index():
    shelf = 'Shelf One'
    boxes = [
        {
            'label': 'A1',
            'content': 'stuff A'
        },
        {
            'label': 'A2',
            'content': 'stuff B'
        }
    ]
    return render_template('index.html', title='Home', shelf=shelf, boxes=boxes)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        # db.session.commit()
        flashing_message = 'Upload requested'
        flash(flashing_message)
        return redirect('/index')
    return render_template('upload.html', title='Upload', form=form)
