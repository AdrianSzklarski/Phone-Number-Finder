from flask import Flask, render_template
import random

app = Flask(__name__)

counter = 0
array = []
index = random.randint(1, 2000)
while counter < index:
    array.append(random.randint(111111111, 999999999))
    counter += 1


@app.route('/')
def homepage():

        return render_template("index.html", len=counter, array=array, index=index-1)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)


