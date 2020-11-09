"""
    Flask - Light Weight Web App FW
    Web App Development with Python
    PreRequisite: HTML + CSS + JavaScript (w3schools)

    Documentation Link: https://flask.palletsprojects.com/en/1.1.x/

    Installation: pip install Flask

    Django -> pretty much industrial for developing larger web apps

"""

from flask import Flask

# Create Your WebApp by constructing Flask Object
app = Flask(__name__)

# App Routing -> Create Routes
# With Decorator @app.route()

@app.route("/")
def index_page():
    message = "Welcome to Flask Web App"
    return message # returning Text

@app.route("/welcome")
def welcome_page():
    message = """
    <html>
        <body>
            <center>
                <h3>Welcome to Flask Web App</h3>
                Register
                <br/>
                Login
            </center>    
        </body>
    </html>        
    """
    return message # returning HTML

# Execute the App
if __name__ == '__main__':
    app.run()   # execute the web app on the Flask Server :)