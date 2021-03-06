from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
    Bestplayers = ["LEBRON JAMES", "Cristiano ronaldo", "Karim Benzema", "Kevin durant", "Tom Brady"]
    return render_template("index.html", Bestplayer=Bestplayers)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", username=name)

#Custom error pages

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500        