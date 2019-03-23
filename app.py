from flask import Flask, request
from model.comparer import Comparer
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/compare', methods=['POST'])
def compare():
    if request.method == 'POST':

        data = request.json
        a = data['a']
        b = data['b']
        c = Comparer()
        c.model.run_pipeline(a, b)

        return('a: ' + str(a) + '\nb: ' + str(b) + '\n%s\n' % str(c.model.outputs))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
