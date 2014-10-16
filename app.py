from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Apache Stratos Python 2.7 Cartridge! Hi again... :)"

if __name__ == "__main__":
    app.run()