from flask import Flask, request
from downloadImage import downloadimages

app = Flask("System delivery")


@app.route("/", methods=["GET"])
def helloWord():
   # downloadimages("Xdelssy delivery juazeiro bahia")
    return "Hello"


app.run()
