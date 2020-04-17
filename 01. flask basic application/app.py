from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
