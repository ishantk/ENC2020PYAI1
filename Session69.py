"""
    Flask
        HTTP Requests - GET and POST
        File Uploads

        For Designing:
            Refer Bootstrap or Material Designs
            https://www.w3schools.com/bootstrap/
            https://material.io
"""

from flask import *

app = Flask("MyApp")

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/login", methods=["POST", "GET"])
@app.route("/login", methods=["POST"])
def authenticate():
    email = request.form["txtEmail"]
    password = request.form["txtPassword"]

    # authenticate the user from the database :)
    if email == "john@example.com" and password == "123456":
        return redirect(url_for("welcome"))
    else:
        return "INVALID CREDENTIALS. Please Try Again"


@app.route("/register-user", methods=["POST"])
def register():
    name = request.form["txtName"]
    email = request.form["txtEmail"]
    password = request.form["txtPassword"]

    # Insert the data in database

    return "{} Registered with Us".format(name)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/register")
def register_user():
    return render_template("register.html")

@app.route("/upload-dataset", methods=["POST"])
def upload_dataset():
    # if request.method == "POST": # we can check the methods as well in the function if we wish to
    file = request.files["dataset"]
    file.save(file.filename)
    # return "DataSet {} Uploaded Successfully".format(file.filename)
    return render_template("upload-success.html", name=file.filename)


@app.route("/upload-image", methods=["POST"])
def upload_image():
    file = request.files["image"]
    file.save(file.filename)
    # return "Image {} Uploaded Successfully".format(file.filename)
    return render_template("upload-success.html", name=file.filename)


if __name__ == '__main__':
    app.run(debug=True)

# Assignment
# Link the DataBases :) either firebase or mongo db