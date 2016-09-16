from flask import Flask,render_template,request, redirect

app = Flask(__name__)
app.secret_key = "fred"

# tmnt ={
#     "red":"raphael.jpg",
#     "yellow":"michelangelo.jpg",
#     "blue":"donatello.jpg",
#     "purple":"leonardo.jpg",
#     "all":1
# }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja/<color>')
def ninja(color):
    tmnt ={
        "red":1,
        "yellow":1,
        "blue":1,
        "purple":1,
        "all":1
    }
    if not tmnt.has_key(color):
        color= "notApril"
    print color

    return render_template('ninja.html',color=color)

@app.route('/ninja')
def colorNinja():
    return redirect("/ninja/all")

app.run(debug=True)
