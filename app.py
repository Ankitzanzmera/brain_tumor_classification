import os
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
from brain_tumor_classification.pipelines.predict import PredictionPipeline
from brain_tumor_classification.utils.common import decodeImage

os.putenv("LANG","en_US.UTF-8")
os.putenv("LC_ALL","en_US.UTF-8")

class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputimage.jpg"
        self.classifier = PredictionPipeline(self.filename)

app = Flask(__name__)
CORS(app)


@app.route("/",methods = ["GET"])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train",methods = ["GET","POST"])
@cross_origin()
def trainroute():
    os.system("python main.py")
    return "Training Done Successfully"

@app.route("/predict",methods = ["POST","GET"])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image,clapp.filename)
    result = clapp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clapp = ClientApp()
    app.run(host="0.0.0.0",port = 80)
