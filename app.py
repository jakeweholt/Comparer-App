from flask import Flask, request, jsonify
from model.comparer import Comparer
from model.matcher import Matcher
from model.string_mapper import MapperDataIn, StringMapper, StringReducer
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


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

@app.route('/match', methods=['POST'])
def match():
    comparison_metric = 'similarity_probability'
    if request.method == 'POST':

        # Get json as dict from input data.
        data = request.json
        x = data['x']
        search_base = data['search_base']

        m = Matcher()

        # Dump to JSON and return
        scores = dict()
        for val in search_base:
            scores[val] = m.model.run_pipeline(x, val)

        max_match = max(scores, key = lambda x: scores.get(x)[comparison_metric])
        response = jsonify({'x':x,
                            'most_likely_match':max_match,
                            'scores':scores})

        return(response)


@app.route('/string_mapper', methods=['POST'])
def string_mapper():
    if request.method == 'POST':
        # Get json as dict from input data.
        data = request.json
        dirty_data = data['dirty_data']
        clean_data_map = data['clean_data_map']

        t = MapperDataIn(clean_data_map, dirty_data)
        m = StringMapper(t)
        m.map()
        sr = StringReducer(m)
        sr.reduce()

        return sr.dataframe_output.to_json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
