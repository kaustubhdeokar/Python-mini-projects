from flask import Flask, request, render_template

import entries

app = Flask(__name__)
valid_entries = entries.fetch_entries()


@app.route("/")
def insert_document():
    return render_template('hello.html')


def show_login_form():
    return render_template('login.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    print('in the login method. ')
    if request.method == 'POST':
        entries.insert_into_collection(request.form.get("name"), request.form.get("password"))
        return render_template('about.html')
    return show_login_form()


@app.route("/update/<user>")
def update(user):
    entries.update_user(user)
    return render_template('login.html')

@app.route("/list")
def list_entries():
    documents = entries.fetch_entries()
    return render_template('list.html', documents=documents)


@app.route("/delete/<user>")
def delete_user(user):
    entries.delete_user(user)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
