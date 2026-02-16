from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='statics')


@app.get('/')
def index():
    context = {
        "fullname": "Pedram Pourhakim"
    }
    return render_template('index.html',context= context)

