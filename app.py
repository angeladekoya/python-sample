from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to samuel's website !!!</h1>"


@app.route('/animal')
def animal():
    animals = ["dog"," kangaroo", "cat", "deer", "lion"]
    return render_template("animal.html", animal=animals) 

@app.route('/product')
def product():
    products = ["nivea","phone", "milk", "cabbage", "pizza"]
    return render_template("products.html", product=products) 

@app.route('/stationary')
def stationary():
    stationary = ["Glue stick","Calculator", "Ruler", "Pencil", "Pen"]
    return render_template("stationary.html", stationary=stationary) 

@app.route("/school")
def contact():
    email="check4obi@yahoo.com"
    mobile="2347036483444"
    return "These are the schools contact details" + email + "," + mobile

@app.route("/calculate")
def calculate():
    a = 56
    b = 34
    sum = a + b
    return "This is the sum total:" + str(sum)


if __name__ == '__main__':

    app.run(debug=True, port=3001,host="0.0.0.0")