from flask import Flask, request, render_template, jsonify
from functions import check_syllable
from functions import check_word
from functions import latin_to_hiragana
from functions import hiragana_english

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test_page.html')

@app.route('/result_function1', methods=['POST'])
def result_function1():
    syllable = request.form.get('function1Input')
    result = check_syllable(syllable)
    return jsonify({'result': result})

@app.route('/result_function2', methods=['POST'])
def result_function2():
    word = request.form.get('function2Input')
    result = check_word(word)
    return jsonify({'result': result})

@app.route('/result_function3', methods=['POST'])
def result_function3():
    jpword = request.form.get('function3Input')
    result = latin_to_hiragana(jpword)
    return jsonify({'result': result})

@app.route('/result_function4', methods=['POST'])
def result_function4():
    jpword = request.form.get('function4Input')
    result = hiragana_english(jpword)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
