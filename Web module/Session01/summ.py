from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return("Let's do some math")

@app.route("/sum/<int:a>/<int:b>")
def calc(a, b):
    return str(a+b)

if __name__ == '__main__':
  app.run(debug=True)
