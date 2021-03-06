# import "packages" from flask
from flask import Flask, render_template, request, redirect
from __init__ import app
from cruddy.app_crud import app_crud

from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /Volunteering path to render Volunteering.html
@app.route('/Volunteering/')
def volunteering():
    return render_template("Volunteering.html")


@app.route('/Announcements/')
def announcements():
    return render_template("Announcements.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/HikingEquipment/')
def equipment():
    return render_template("equipment.html")

@app.route("/hikeDescriptionOutline", methods=["GET", "POST"])
def hikeDescriptionOutline():
    return render_template("hikeDescriptionOutline")

@app.route('/mainmap/')
def mainmap():
    return render_template("/interactivemapcode/mainmap.html")

@app.route('/Forum/')
def Forum():
    return render_template("Forum.html")

@app.route('/AboutTN/')
def AboutTN():
    return render_template("AboutTN.html")

@app.route('/AboutTNLeadership/')
def AboutTNLeadership():
    return render_template("AboutTNLeadership.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
