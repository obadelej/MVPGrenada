from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load_index():
    return render_template("index.html")



if app.name == "__main__":
    app.run(debug=True)