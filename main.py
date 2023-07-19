from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    requested_post = None

    respone = requests.get(
        "https://newsdata.io/api/1/news?country=lb&category=top&apikey=pub_2533162b45f4c0a11f07b5ff4f72d54244c30")
    data_json = respone.json()
    posts = data_json['results']
    return render_template("index.html", all_posts=posts)


@app.route("/sports")
def sports():
    respone = requests.get(
        "https://newsdata.io/api/1/news?country=lb&category=sports&apikey=pub_2533162b45f4c0a11f07b5ff4f72d54244c30")
    data_json = respone.json()
    posts = data_json['results']
    return render_template('sports.html', all_sports=posts)


@app.route("/technology")
def technology():
    respone = requests.get(
        "https://newsdata.io/api/1/news?country=lb&category=technology&apikey=pub_2533162b45f4c0a11f07b5ff4f72d54244c30")
    data_json = respone.json()
    posts = data_json['results']
    return render_template('technology.html', all_technology=posts)


@app.route("/health")
def health():
    response = requests.get("https://newsdata.io/api/1/news?country=lb&category=health&apikey=pub_2533162b45f4c0a11f07b5ff4f72d54244c30")
    data_json = response.json()
    posts = data_json['results']
    return render_template('health.html', all_health=posts)


@app.route("/environment")
def environment():
    response = requests.get(
        "https://newsdata.io/api/1/news?country=lb&category=environment&apikey=pub_2533162b45f4c0a11f07b5ff4f72d54244c30")
    data_json = response.json()
    posts = data_json['results']
    return render_template('environment.html', all_environment=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    fromaddr = "al.khezana.lb@gmail.com"
    password = "ostmfdyhpccizbam"
    toaddr = "abdallahadam130@gmail.com"

    with smtplib.SMTP('smtp.gmail.com:587') as connection:
        connection.starttls()
        connection.login(user=fromaddr, password=password)
        connection.sendmail(fromaddr, password, email_message)


if __name__ == "__main__":
    app.run(debug=True)
