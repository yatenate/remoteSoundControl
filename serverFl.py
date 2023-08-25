from flask import Flask, render_template
import pyautogui

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/mute")
def mute():
    response = "Muting"
    pyautogui.press('volumemute')
    return response


@app.route("/disconnect")
def disconnect():
    response = "Turning volume up..."
    return response


@app.route("/down")
def down():
    pyautogui.press("volumedown")
    response = "Turning volume up..."
    return response


@app.route("/up")
def up():
    pyautogui.press('volumeup')
    response = "Turning volume up..."
    return response

if __name__ == "__main__":
    app.run(debug=True)
