pred_df = data.convert_ip_to_df()
        predict_pipeline = PredictPipeline(pred_df)
        result = predict_pipeline.predict()
        if result == 0:
            res = "P"
        else:
            res = "A"
        print(res)