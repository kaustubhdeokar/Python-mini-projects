from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def main():
    return "main"


@app.route("/form")
def form():
    return render_template('form.html')


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return 'get method'
    else:
        form_data = request.form
        d = {}
        for index, item in enumerate(form_data.values()):
            d["field"+str(index)] = item
        collection.insert_one(d)
        return render_template('data.html', form=form_data)


if __name__ == "__main__":
    cluster = MongoClient(
        "mongodb+srv://kaustubh:kaustubh@cluster0.c5vao.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["nursery"]
    collection = db["notes"]
    app.run(debug=True)
