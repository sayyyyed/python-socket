from distutils import core
from flask import Flask, render_template
from flask_socketio import SocketIO, send
# test
app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)

@app.route("/")
def message():
    return render_template("message.html")

if __name__ == "__main__":
    app.run(debug=True)
