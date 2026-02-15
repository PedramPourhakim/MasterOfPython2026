from flask import Flask,request

app = Flask(__name__)

# if the name of the file is app.py or wsgi.py then no need
# to write flask run --host= 0.0.0.0
@app.route("/",methods=["GET","POST"])
def index():
    app.logger.debug(f"A value for debugging")
    if request.method == "POST":
        return "nothing"
    else:
        return "<p>Index page</p>"


# for running the application we have to write this command in the console : flask --app main run
# flask --app main run --host 0.0.0.0
# flask --app main run --host 0.0.0.0 --port 8000

# debug mode for getting reactive result
# flask --app main run --host 0.0.0.0 --port 8000 --debug


@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"

@app.route('/projects/')
def projects():
    return "<p>Project page</p>"



# print(url_for('index'))