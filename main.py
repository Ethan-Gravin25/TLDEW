# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /Volunteering path to render Volunteering.html
@app.route('/Volunteering/')
def Volunteering():
    return render_template("Volunteering.html")


@app.route('/Announcements/')
def Announcements():
    return render_template("Announcements.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

#test


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/HikingEquipment/')
def equipment():
    return render_template("equipment.html")

@app.route('/hikeDescriptionOutline/')
def hikeDescriptionOutline():
    return render_template("hikedescriptionOutline.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
