from flask import Flask, render_template, request, redirect
import random

# flask run --host=0.0.0.0 --port=80
max_number = 999999999
min_number = 111111111

app = Flask(__name__)

counter = 0
array = []
index = random.randint(1, 18)
while counter < index:
    array.append(random.randint(min_number, max_number))
    counter += 1


@app.route('/', methods=('GET', 'POST'))
def homepage():
    return render_template("index.html",  len=counter, array=array, index=index)


@app.route('/', methods=('GET', 'POST'))
def click():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('/', name=name)
    elif request.method == 'GET':
        return '<h1>Stop, is not safe</h1>'


@app.route('/phonenumbers', methods=('GET', 'POST'))
def phonenumbers():
    if request.method == "POST":
        number = request.form["quantity"]
        if int(number) in array:
            massage = f'''The number is in the list'''
        else:
            massage = f'''The number is not in the list'''
    return render_template("phonenumbers.html", massage=massage, len=counter, array=array)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


