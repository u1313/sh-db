from flask import render_template
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

@app.route('/upload')
def upload():
    form = UploadForm()
    return render_template('upload.html', title='Upload', form=form)
