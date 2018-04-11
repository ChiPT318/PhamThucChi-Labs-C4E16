import mlab
from flask import *
from models.service import Service
from models.users import User
from models.orders import Order
import datetime

app = Flask(__name__)
app.secret_key = "Da Key"
mlab.connect()


# new_service = Service(name="Ka", yob=2002, gender=0,
# height=148, phone="0912450834", address="HD", status=False)

# new_service.save()

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/search/<int:gender>")
def search(gender):
    all_services = Service.objects(gender=gender)
    # k_a = all_services[0]
    return render_template("search.html", all_services = all_services)


@app.route("/admin")
def admin():
    services = Service.objects()
    return render_template("admin.html", services = services)

@app.route("/delete/<service_id>")
def delete(service_id):
    print(service_id)
    service_to_delete = Service.objects.with_id(service_id)

    if service_to_delete is None:
        return("Not found")
    else:
        service_to_delete.delete()
        return redirect(url_for("admin"))


@app.route("/detail/<service_id>/")
def detail(service_id):

    service_to_show = Service.objects.with_id(service_id)

    if service_to_show is None:
        return("Not found")
    else:
        return render_template("details.html", service = service_to_show)


@app.route("/new_service", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']

        new_service = Service(name = name, yob= yob, address =address, gender = gender)
        new_service.save()
        return redirect(url_for("admin"))


@app.route("/update-service/<service_id>", methods=["GET", "POST"])
def update(service_id):
    if request.method == "GET":
        service = Service.objects.with_id(service_id)
        return render_template("updating.html", service = service)

    elif request.method == "POST":
        form = request.form
        service = Service.objects.with_id(service_id)
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']

        service.update(set__name= name, set__yob= yob, set__address= address, set__gender= gender)
        service.reload()
        return redirect(url_for("admin"))


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        form = request.form
        name = form["name"]
        email = form["email"]
        username = form["username"]
        password = form["password"]
        status = True

        new_user = User(name=name, email=email, username=username, password=password, status = status)
        new_user.save()
        session["logged_in"] = True
        return redirect(url_for("index"))



@app.route("/login/<int:gender>", methods=["GET", "POST"])
def login(gender):
    if request.method == "GET":
        if session["logged_in"] == True:
            return redirect(url_for("search", gender = gender))
        else:
            return render_template("login.html")
    else:
#         form = request.form
#         username = form["username"]
#         password = form["password"]
# #
#         all_users = User.objects()
#         for user in all_users:
#             if username == user["username"] and password == user["username"]:
#                 session["logged_in"] = True
#                 return redirect(url_for("search", gender=gender))

        return render_template("error.html")

@app.route("/order/<service_id>/")
def order(service_id):
    if user not in session:
        return redirect(url_for('login'))
    else:
        service_id = Service.objects.with_id(service_id)
        user_id = session["user.id"]
        time = str(datetime.now())
        status = False

        new_order = Order(service_id = service_id, user_id = user_id, time = time, status = status)
        new_order.save()
        return "Da gui Yeu Cau"

if __name__ == '__main__':
  app.run(debug=True)
