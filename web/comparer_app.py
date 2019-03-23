from flask import Flask, request
import pickle
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
        c = pickle.load(open("serialized_models/c_model.p", "rb"))
        c.model.run_pipeline(a, b)

        return('a: ' + str(a) + '\nb: ' + str(b) + '\n%s\n' % str(c.model.outputs))
