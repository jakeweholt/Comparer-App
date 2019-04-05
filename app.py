from flask import Flask, request, jsonify
from model.comparer import Comparer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/compare', methods=['POST'])
def compare():
    if request.method == 'POST':

        # Get json as dict from input data.
        data = request.json
        a = data['a']
        b = data['b']

        # Confirm vectors are same length, have same headers.
        assert(list(a) == list(b))

        # Use Comparer to run comparison metrics over each value.
        c = Comparer()
        output = dict()
        output['a'] = a
        output['b'] = b
        for column in list(a):
            output[column] = c.model.run_pipeline(a[column], b[column])

        # Dump to JSON and return
        response = jsonify(output)

        return(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
