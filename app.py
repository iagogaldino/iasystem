from flask import Flask, request

# from downloadImage import downloadimages

print("Iniciando aplicação......")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello"


print("run......")
app.run()
