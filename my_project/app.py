from flask import Flask, request, render_template, jsonify
from functions import check_syllable
from functions import check_word
from functions import latin_to_hiragana
from functions import english_translation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""

    if request.method == 'POST':
        # Determine which function to call based on a hidden input in the form
        action = request.form.get('action')
        print(action)
        if action == 'function1':
            syllable = request.form.get('function1Input')
            result1 = check_syllable(syllable)
        elif action == 'function2':
            word = request.form.get('function2Input')
            result2 = check_word(word)
        elif action == 'function3':
            jpword = request.form.get('function3Input')
            result3 = latin_to_hiragana(jpword)
        elif action == 'function4':
            jpword = request.form.get('function4Input')
            result4 = english_translation(jpword)

    return render_template('index.html', result1=result1, result2=result2, result3=result3, result4=result4)

if __name__ == '__main__':
    app.run(debug=True)
