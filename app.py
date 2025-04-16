from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return "<h3> Greetings welcome to Angel's digital world !!!</h3>"


@app.route('/animal')
def animal():
    animals = ["dog"," kangaroo", "cat", "deer", "chimpanzee", "dinosaur", "moa"]
    return render_template("animal.html", animal=animals) 

@app.route('/books')
def book():
    books= ["cinderella", "rapunzel", "tym", "tyu", "yolo", "sil"]
    return render_template("books.html", book=books)

@app.route('/cities')
def cities():
    cities=["bfd", "ldn", "ncl", "mgm", "lpl", "lsr"]
    return render_template("cities.html", city=cities)

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