from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data = CustomData(
            MDVP_Fo_Hz=request.form.get('fo', type=float),
            MDVP_Fhi_Hz=request.form.get('fhi', type=float),
            MDVP_Flo_Hz=request.form.get('flo', type=float),
            MDVP_Jitter_Percent=request.form.get('jitter', type=float),
            MDVP_Jitter_Abs=request.form.get('absjitter', type=float),
            MDVP_RAP=request.form.get('rap', type=float),
            MDVP_PPQ=request.form.get('ppq', type=float),
            Jitter_DDP=request.form.get('ddp', type=float),
            MDVP_Shimmer=request.form.get('shimmer', type=float),
            MDVP_Shimmer_dB=request.form.get('shimmerdb', type=float),
            Shimmer_APQ3=request.form.get('apq3', type=float),
            Shimmer_APQ5=request.form.get('apq5', type=float),
            MDVP_APQ=request.form.get('apq', type=float),
            Shimmer_DDA=request.form.get('dda', type=float),
            NHR=request.form.get('nhr', type=float),
            HNR=request.form.get('hnr', type=float),
            RPDE=request.form.get('rpde', type=float),
            DFA=request.form.get('dfa', type=float),
            spread1=request.form.get('spread1', type=float),
            spread2=request.form.get('spread2', type=float),
            D2=request.form.get('d2', type=float),
            PPE=request.form.get('ppe', type=float)
        )

        pred_df = data.convert_ip_to_df()
        predict_pipeline = PredictPipeline(pred_df)
        result = predict_pipeline.predict()
        if result[0] == 0.:
            res = "Negative"
        else:
            res = "Positive"
        print(result)
        return render_template('index.html', res=res)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)        