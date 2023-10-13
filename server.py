import openai as openai
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
# api_key = 'YOUR_API_KEY'
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key


@app.route('/api', methods=['GET'])
def hello1():
    return jsonify({'message': 'Hello, this is your REST API!'})


@app.route('/api/hello/<question>', methods=['GET'])
def hello(question):    
    answer = chatGptResponse(question)
    return jsonify({'message': answer})


def chatGptResponse(question):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
    return response['choices'][0]['message']['content']

app.run()