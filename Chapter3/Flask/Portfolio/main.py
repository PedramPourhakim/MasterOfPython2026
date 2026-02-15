from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='statics')


@app.get('/')
def index():
    return render_template('index.html')

@app.get('/contact')
def contact():
    return "Contact Page"
