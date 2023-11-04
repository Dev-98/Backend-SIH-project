from flask_cors import CORS
import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

CORS(app)

carrier = {
    "E": "Engineering",
    "H": "Medical/Healthcare",
    "T": "Teaching/Research",
    "D": "Data Analysis/Statistics",
    "A": "Arts/Creative Industries",
    "B": "Business/Entrepreneurship",
    "L": "Law/Legal Professions",
    "S": "Sports and Coaching",
    "R": "Science and Research",
    "C": "Social Services and Counseling",
}

def find_max_word_and_sum(numbers_with_words):

    word_sums = {}
    total = 0
    
    for item in numbers_with_words:
        clean_item = item.strip().strip('"').strip("'")
        # print(clean_item)

        number = int(clean_item[0])
        word = clean_item[-1]
        
        total += number

        if word in word_sums:
            word_sums[word] += number
        else:
            word_sums[word] = number
    
    
    return total, word_sums


# numbers_with_words =  

@app.route("/")
def hello():
    return "Hello world"
    # return render_template("index.html")


@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == "POST":
        t = request.form.get("output").replace("[","").replace("]", "")
        test = t.split(',')

        denomino, max_word = find_max_word_and_sum(test)
        words = list(max_word.keys())
    
        final = {}
        for i in words:
            percent = (max_word[i] / denomino) * 100

            final[carrier[i]] = int(round(percent, 2))

        
        return jsonify(final)
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
