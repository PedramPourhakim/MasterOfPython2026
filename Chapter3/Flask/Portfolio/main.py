from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__,
            template_folder='templates',
            static_folder='statics')


@app.get('/')
def index():

    context = {
        "message" : request.args.get('message', ""),
        "fullname": "Pedram Pourhakim"
    }
    return render_template('index.html',context= context)



@app.post('/contact')
def contact():
    app.logger.debug(request.form.get('name'))
    return redirect(url_for('index',message="ticket successfully submitted, I will contact you later."))
