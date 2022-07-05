from flask import Flask, render_template, request

from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "jesutofunmisokunleproject@gmail.com"
app.config['MAIL_PASSWORD'] = "qwertyuiop1."
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = "To the world of JT Sports"
        msg = "Thank you for subscribing to JT. Stay tuned for more information" 

        message = Message(
            subject, sender="jesutofunmisokunleproject@gmail.com", recipients=[email])

        message.body = msg

        mail.send(message)

        success = "Thank you for Subscribing"

        return render_template("result.html", success=success)


if __name__ == "__main__":
    app.run(debug=True)
