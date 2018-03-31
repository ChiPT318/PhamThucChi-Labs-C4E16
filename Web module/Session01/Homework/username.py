from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<person>')
def user(person):

    persons = [
    {"Name" : "Chi",
    "Work" : "Babysitter",
    "Hobbies" : "Youtube"
    },
    {"Name" : "A",
    "Work" : "Armyman",
    "Hobbies" : "Guns"
    },
    {"Name" : "B",
    "Work" : "Buttermaker",
    "Hobbies" : "Dairy"}
    ]

    for users in persons:
            if person == users["Name"]:
                person = users
                return render_template('info.html', person = person)
    return render_template("not found.html")


if __name__ == '__main__':
  app.run(debug=True)
