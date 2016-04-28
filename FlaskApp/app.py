from flask import Flask, render_template, url_for
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


@app.route("/")
def main():
    return render_template('index.html')

# url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()