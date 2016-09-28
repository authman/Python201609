from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index1.html", phrase="Error!", times=100)
app.run(debug=True)
