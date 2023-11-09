from flask import Flask, render_template, redirect, request, url_for
import random
import smtplib
otp = 0

app = Flask(__name__, template_folder='templete')


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/signup_page.html", methods=['GET', 'POST'])
def signup_page():
    global otp
    my_email = "codewithmrpy@gmail.com"
    password = "eaflyqlwydcznrgt"
    if request.method == "POST":
        otp = random.randint(100000, 999999)
        email = request.form['email']
        # password1 = request.form['password']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"subject:Your signup OTP \n\n {otp}")
        return redirect(url_for('OTP_a', email=email, otp=otp))
    else:
        pass
    return render_template("signup_page.html")


@app.route("/OTP_a.html", methods=['GET', 'POST'])
def OTP_a():
    global otp
    email = request.args.get('email', None)
    otp = str(otp)
    if request.method == "POST":
        u_otp = request.form['U_otp']
        if otp == u_otp:
            return redirect(url_for('home'))
        else:
            return render_template("failed.html")

    return render_template('OTP_a.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)
