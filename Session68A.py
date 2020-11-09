from flask import *

app = Flask("LMS")

# we will have 3 different users to use LMS
# 1. Student
# 2. Trainer
# 3. Admin

@app.route("/")
def index():
    message = """
    <html>
        <body>
            <center>
                <h3>Welcome to LMS</h3>
                Register
                <br/>
                Login
            </center>    
        </body>
    </html>        
    """
    return message # returning HTML


@app.route("/student")
def student():
    # html = """
    #     <html>
    #         <body>
    #             <center>
    #                 <h3>Welcome to LMS - Student</h3>
    #                 <h4>Please Login to Your Account</h4>
    #                 <form>
    #                     <input type='text' name='txtPhone' placeholder='Enter Your Phone Number'/>
    #                     <br/>
    #                     <input type='text' name='txtOTP' placeholder='Enter OTP'/>
    #                     <br/>
    #                     <input type='submit' value='LOGIN STUDENT'/>
    #                 </form>
    #             </center>
    #         </body>
    #     </html>
    # """
    # return html

    return render_template("register-student.html")

@app.route("/trainer")
def trainer():
    html = """
        <html>
            <body>
                <center>
                    <h3>Welcome to LMS - Trainer</h3>
                    <h4>Please Login to Your Account</h4>
                    <form>
                        <input type='text' name='txtPhone' placeholder='Enter Your Trainer ID'/>
                        <br/>
                        <input type='text' name='txtOTP' placeholder='Enter OTP Sent on Phone'/>
                        <br/>
                        <input type='submit' value='LOGIN TRAINER'/>
                    </form> 
                </center>    
            </body>
        </html>     
    """
    return html

@app.route("/admin")
def admin():
    html = """
        <html>
            <body>
                <center>
                    <h3>Welcome to LMS - Admin</h3>
                    <h4>Please Login to Your Account</h4>
                    <form>
                        <input type='text' name='txtPhone' placeholder='Enter Your Admin ID'/>
                        <br/>
                        <input type='text' name='txtOTP' placeholder='Enter OTP sent on Your Phone'/>
                        <br/>
                        <input type='submit' value='LOGIN ADMIN'/>
                    </form> 
                </center>    
            </body>
        </html>     
    """
    return html


@app.route("/<type>")
def user(type):
    if type == 'stu':
        # return "Hello Student", type
        return redirect(url_for('student'))
    elif type == 'tra':
        # return "Hello Trainer", type
        return redirect(url_for('trainer'))
    elif type == 'adm':
        # return "Hello Admin", type
        return redirect(url_for('admin'))
    else:
        return "INVALID OR BAD REQUEST"


if __name__ == '__main__':
    app.run(debug=True)


# Assignment:
# Take the details from Student as Name, Phone, Email, Gender, City, State etc..
# on the HTML Web Page and Save it to the MongoDB or Firestore