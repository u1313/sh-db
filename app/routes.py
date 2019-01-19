from flask import render_template
from app import app

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
