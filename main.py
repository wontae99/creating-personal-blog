from flask import Flask, render_template, request
import requests
import smtplib, ssl
import os

app = Flask(__name__)
#POST DATA
n_point_url = "https://api.npoint.io/73007b8dc2f982558f95"
post_data = requests.get(n_point_url).json()
# GMAIL ACCOUNT INFO
OWN_EMAIL = os.environ.get('OWN_EMAIL')
OWN_PASSWORD = os.environ.get('OWN_PASSWORD')
GMAIL_SMTP_SERVER = "smtp.gmail.com"
PORT = 465
context = ssl.create_default_context()

@app.route('/')
def home():
    return render_template("index.html", data=post_data)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", sent=True)
    else:
        return render_template("contact.html", sent=False)

@app.route('/post/<int:index>')
def post_page(index):
    requested_post = None
    for post in post_data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP_SSL(GMAIL_SMTP_SERVER, PORT, context=context) as connection:
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=GMAIL_SMTP_SERVER, to_addrs='', msg=email_message)

if __name__ == "__main__":
    app.run()