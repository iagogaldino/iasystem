from flask import Flask, request

# from downloadImage import downloadimages

print("Iniciando aplicação......")

app = Flask(__name__)


@app.route("/teste", methods=["GET"])
def helloWord():
    # downloadimages("Xdelssy delivery juazeiro bahia")
    return "Hello"


print("run......")
app.run()
