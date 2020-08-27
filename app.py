#app to deploy model and predict the spam

#importing important libraries

from flask import Flask, request, jsonify, render_template
from clean_text import clean_mesaage
import pickle

app = Flask(__name__) #Creating app

#Loading models from pickle

classifier = pickle.load(open('classifier_model.pkl','rb'))
cv = pickle.load(open('countverctorizer.pkl','rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        message = request.form['message']
        message = clean_mesaage(message)
        message = [message]
        vect = cv.transform(message)
        my_prediction = classifier.predict(vect)
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    #app.run(port=6011)
    app.run()

