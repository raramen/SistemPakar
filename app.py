from flask import Flask, render_template, request
from fuzzylogic import process_inputs
#
# fuzzy_labels

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/hasil', methods=['POST'])
def hasil():
    responses = request.form.to_dict()
    prediction, fuzzy_results = process_inputs(responses)
    
    categorical_options = [
        'sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'
    ]
    return render_template(
        'newoutput.html',
        prediction=prediction,
        responses=responses,
        categorical_options=categorical_options,
        fuzzy_labels=fuzzy_results
    )

if __name__ == '__main__':
    app.run(debug=True)