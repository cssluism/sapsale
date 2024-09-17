import pickle
import numpy as np
from flask import Flask, request

# Creates Flask serving engine
app = Flask(__name__)

model = None
appHasRunBefore = False


 VL_YEAR_SALEHD  = ""
  VL_MONTH_SALEHD = "" 
   VL_CURRENCY_SALEHD = ""
 VL_YEAR_SALEIT = ""
  VL_MONTH_SALEIT = ""
  VL_PARTNERID_CLIENT_SO = ""
 VL_CURRENCY_SALEITEM = ""
 VL_PRODUCTID = ""
 VL_PRODCATEGORYID = ""


@app.before_request
def init():
    """
    Load model else crash, deployment will not start
    """
    global model
    global appHasRunBefore

    if not appHasRunBefore:
        # All the model files will be read from /mnt/models
        model = pickle.load(open('/mnt/models/model.pkl', 'rb'))
        # model = pickle.load(open('model.pkl', 'rb'))
        appHasRunBefore = True
        return None


@app.route("/v2/check", methods=["GET"])
def status():
    global model
    if model is None:
        return "Flask Code: Model was not loaded."
    else:
        return "Flask Code: Model loaded successfully."


@app.route("/v2/predict", methods=["POST"])
def predict():
    global model
    global flower
    global VL_YEAR_SALEHD, VL_MONTH_SALEHD, VL_CURRENCY_SALEHD
    global VL_YEAR_SALEIT, VL_MONTH_SALEIT, VL_PARTNERID_CLIENT_SO
    global VL_CURRENCY_SALEITEM, VL_PRODUCTID, VL_PRODCATEGORYID



    
    print("Docker image version is 4.0")

    if model is None:
        return "Flask Code: Model was not loaded."
    else:
        query = dict(request.json)

VL_YEAR_SALEHD = query["YEAR_SALEHD"]
VL_MONTH_SALEHD = query["YEAR_SALEHD"]
VL_CURRENCY_SALEHD = query["CURRENCY_SALEHD"]
VL_YEAR_SALEIT = query["YEAR_SALEIT"]
VL_MONTH_SALEIT = query["MONTH_SALEIT"]
VL_PARTNERID_CLIENT_SO = query["PARTNERID_CLIENT_SO"]
VL_CURRENCY_SALEITEM = query["CURRENCY_SALEITEM"]
VL_PRODUCTID = query["PRODUCTID"]
VL_PRODCATEGORYID = query["PRODCATEGORYID"]

        
        attributes = [VL_YEAR_SALEHD,VL_MONTH_SALEHD,VL_CURRENCY_SALEHD,VL_YEAR_SALEIT,VL_MONTH_SALEIT,VL_PARTNERID_CLIENT_SO,VL_CURRENCY_SALEITEM,VL_PRODUCTID,VL_PRODCATEGORYID ]
        print("Attributes: ", [attributes])
        prediction = model.predict(
            # (trailing comma) <,> to make batch with 1 observation
            [attributes]
        )
        
      
        return {"attributes": {"YEAR_SALEHD": VL_YEAR_SALEHD, "MONTH_SALEHD": VL_MONTH_SALEHD, "CURRENCY_SALEHD": VL_CURRENCY_SALEHD, "YEAR_SALEIT": VL_YEAR_SALEIT, "MONTH_SALEIT": VL_MONTH_SALEIT,"PARTNERID_CLIENT_SO": VL_PARTNERID_CLIENT_SO, "CURRENCY_SALEITEM": VL_CURRENCY_SALEITEM, "PRODUCTID": VL_PRODUCTID, "PRODCATEGORYID": VL_PRODCATEGORYID
         
         }, 
         "predection": prediction}


if __name__ == "__main__":
    print("Serving Initializing")
    init()
    print("Serving Started")
    app.run(host="0.0.0.0", debug=True, port=9001)
    # app.run(debug=True)
