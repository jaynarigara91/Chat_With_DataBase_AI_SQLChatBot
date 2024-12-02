from flask import Flask, jsonify
from Chat_With_SQL import ChatWithSQL

app = Flask(__name__)

obj = ChatWithSQL("root","Jayesh@91","localhost","pizzahut")

@app.route('/send-message', methods=['GET'])
def send_message():
    # message = "Hello, this is a message from the Flask API!"
    message = obj.Message("How many orders we get?")
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')