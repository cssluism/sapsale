import pickle
import numpy as np
import pandas as pd
from flask import Flask, request


# Creates Flask serving engine
app = Flask(__name__)

model = None
appHasRunBefore = False

vl_year_salehd = ""
vl_month_salehd = "" 
vl_currency_salehd = ""
vl_year_saleit = ""
vl_month_saleit = ""
vl_partnerid_client_so = ""
vl_currency_saleitem = ""
vl_productid = ""
vl_prodcategoryid = ""



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
    global vl_year_salehd, vl_month_salehd, vl_currency_salehd
    global vl_year_saleit, vl_month_saleit, vl_partnerid_client_so
    global vl_currency_saleitem, vl_productid, vl_prodcategoryid

    print("Docker image version is 4.0")

    if model is None:
        return "Flask Code: Model was not loaded."
    else:
        query = dict(request.json)
        vl_year_salehd = query["YEAR_SALEHD"]
        vl_month_salehd = query["MONTH_SALEHD"]
        vl_currency_salehd = query["CURRENCY_SALEHD"]
        vl_year_saleit = query["YEAR_SALEIT"]
        vl_month_saleit = query["MONTH_SALEIT"]
        vl_partnerid_client_so = query["PARTNERID_CLIENT_SO"]
        vl_currency_saleitem = query["CURRENCY_SALEITEM"]
        vl_productid = query["PRODUCTID"]
        vl_prodcategoryid = query["PRODCATEGORYID"]


        
        attributes = [[vl_year_salehd, vl_month_salehd, vl_currency_salehd, vl_year_saleit, vl_month_saleit, vl_partnerid_client_so, vl_currency_saleitem, vl_productid, vl_prodcategoryid]]
        
        

         # Create a DataFrame from the sample input
        sample_df = pd.DataFrame(attributes, columns=['YEAR_SALEHD','MONTH_SALEHD','CURRENCY_SALEHD','YEAR_SALEIT','MONTH_SALEIT','PARTNERID_CLIENT_SO','CURRENCY_SALEITEM','PRODUCTID','PRODCATEGORYID'])


         

        # One-hot encode the sample
        sample_encoded = pd.get_dummies(sample_df, columns=['YEAR_SALEHD','MONTH_SALEHD','CURRENCY_SALEHD','YEAR_SALEIT','MONTH_SALEIT','PARTNERID_CLIENT_SO','CURRENCY_SALEITEM','PRODUCTID','PRODCATEGORYID'])

        # Assuming features_df contains your training data with one-hot encoded columns
        # Reindex to match the training feature set
        sample_encoded = sample_encoded.reindex(columns=features_df.columns, fill_value=0)

# Make the prediction
##predictedvalue = model.predict(sample_encoded)






        # Make the prediction
        print("Attributes: ", attributes)
        prediction = model.predict(
            # (trailing comma) <,> to make batch with 1 observation
            [sample_encoded]
        )
        
        return {"attributes": {"YEAR_SALEHD": vl_year_salehd,"MONTH_SALEHD": vl_month_salehd,"CURRENCY_SALEHD": vl_currency_salehd,"YEAR_SALEIT": vl_year_saleit,"MONTH_SALEIT": vl_month_saleit,"PARTNERID_CLIENT_SO": vl_partnerid_client_so,"CURRENCY_SALEITEM": vl_currency_saleitem,"PRODUCTID": vl_productid,"PRODCATEGORYID": vl_prodcategoryid},"predection": prediction}


if __name__ == "__main__":
    print("Serving Initializing")
    init()
    print("Serving Started")
    app.run(host="0.0.0.0", debug=True, port=9001)
    # app.run(debug=True)
