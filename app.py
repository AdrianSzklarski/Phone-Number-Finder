from flask import Flask, render_template, request, redirect
import random
# flask run --host=0.0.0.0 --port=80

app = Flask(__name__)

counter = 0
array = []
index = random.randint(1, 10)
while counter < index:
    array.append(random.randint(111111111, 999999999))
    counter += 1



@app.route('/')
def homepage():
    return render_template("index.html", len=counter, array=array, index=index)


@app.route('/', methods=('GET', 'POST'))
def click():
    name = request.form['name']
    return render_template('/', name=name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)





