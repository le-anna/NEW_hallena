from flask import Flask, request, jsonify, render_template
import pickle
import time

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

# nender_template('chatbot.html', user_text='You: $ {}'.format(sentence), prediction_text='Bot: $ {}'.format(prediction))


@app.route('/chatbot', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        sentence = request.form.get('sentence')
        print(sentence)
        prediction = ''

        def timer():
            time.sleep(1)
            return True
        if timer() and sentence == 'Hello!':
            prediction = 'Hello, nice to meet you! What is your name?'
        elif timer() and sentence == 'My name is Jane.':
            prediction = 'It is a pleasure to meet you, Jane. Is there anything that is bothering you or something that you would like to discuss with me?'
        elif timer() and sentence == 'I am quite sad.':
            prediction = 'I am sorry to hear that. What is it that is causing this state of mind?'
        elif timer() and sentence == 'I am conflicted as to whether I should seek help.':
            prediction = 'Oftentimes, we are quite reluctant to seek help lest we face humiliation and stigmatization from others. While I am here to listen to your concerns, it would be in your best interest to proceed to further professional services for your current mental state.'
        else:
            prediction = 'Sorry, I did not catch that. Please repeat your message.'
        # return render_template('chatbot.html', user_text='You: {}'.format(sentence))
        return render_template('chatbot.html', prediction_text='Bot: {}'.format(prediction))
    else:
        return render_template('chatbot.html')
