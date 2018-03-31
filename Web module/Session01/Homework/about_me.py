from flask import Flask, render_template, redirect
import os

app = Flask(__name__)


@app.route('/about-me')
def about_me():
    person = {
    "Name" : "Chi",
    "Work" : "Babysitter",
    "Hobbies" : "Youtube"
    }
    return render_template("info.html", person = person)

@app.route("/school")
def school():
    return redirect("http://techkids.vn/", code = 302)
if __name__ == '__main__':
  app.run(debug=True)
