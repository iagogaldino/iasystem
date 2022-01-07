from flask import Flask, request
from downloadImage import downloadimages

app = Flask("System delivery")


@app.route("/helloword", methods=["POST"])
def helloWord():
   # downloadimages("Xdelssy delivery juazeiro bahia")
    return request.get_json()


app.run()
