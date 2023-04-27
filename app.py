from flask import Flask, request, render_template, redirect
from flask import session, make_response

app = Flask(__name__)

# Flask uses a secret key to encrypt cookies used to connect
# the browser to the session--so if you want to use sessions,
# you have to have a secret key. If the public learns this
# value, they can forge session information--so for sites with
# security concerns, make sure this isn't checked into a
# public place like GitHub
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"



# **************************
# SECRET-INVITE DEMO ROUTES:
# **************************


@app.route("/login-form")
def show_login_form():
    """Show form that prompts users to enter the secret access code"""
    return render_template("login-form.html")

@app.route("/login")
def verify_secret_code():

    """
    Checks to see if the entered access code is correct

    - If the code is incorrect, redirect users back to the login form to try again

    - If the code is correct...
        - set session to indicate that user has access
        - redirect to the secret invite
    """
    SECRET = "chickenz_are_gr8"
    entered_code = request.args["secret_code"]
    if entered_code == SECRET:
        session["entered-pin"] = True
        return redirect("/secret-invite")
    else:
        return redirect("/login-form")


@app.route("/secret-invite")
def show_secret_invite():
    """
    Check to see if session contains 'entered-pin' (if user entered the correct secret code)

    - If it does, render the invite template

    - If session['entered-pin'] is missing or False, redirect user to the form to enter the secret code
    """
    if session.get("entered-pin", True):
        return render_template("invite.html")
    else:
        return redirect("/login-form")
