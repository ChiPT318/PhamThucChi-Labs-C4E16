from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') #mo trang chu
def index():   #khi vao trang chu kia thi chay function index luon
    posts = [
    {
    "title" : "Tho con coc",
    "content" : "nekrnk kenjk kejn kenrj kernvw nwin",
    "author" : "Chi",
    "gender" : 0
    },
    {
    "title" : "MamaMia",
    "content" : "Ma ma mia, here we go again. My my, how can I resist ya",
    "author" : "AbbA",
    "gender": 1
    },

    {
    "title" : "Khong biet lam tho",
    "content" : "Chiu chiu",
    "author" : "A Bo Co",
    "gender": 0
    }
    ]

    return render_template("index.html", posts = posts)

@app.route("/hello")
def hello():
    return("Hello C4E16")

@app.route("/sayhi/<name>/<age>")
def sayhi(name, age):
    return("Hi " + name + "You are " +age)


if __name__ == '__main__':
  app.run(debug=True)
