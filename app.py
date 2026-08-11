from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Sanjana Maity - changes "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)