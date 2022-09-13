from fastapi import FastAPI
import uvicorn
import pandas as pd
import pickle

# Set config --> No óptimo
host = "0.0.0.0"
port = 8080
debug = False
reload = False


# Load transformer & model
with open('outputs/transformer.pickle', 'rb') as r:
    transformer = pickle.load(r)
    
with open('outputs/model.pickle', 'rb') as r:
    model = pickle.load(r)

app = FastAPI()

@app.get("/get-iris-type")
def get_iris(
    sepal_length:float,
    sepal_width:float,
    petal_length:float,
    petal_width:float
    ):

    # Build dataset
    data_predict = pd.DataFrame.from_dict(
        data = {
         'sepal length (cm)' : [sepal_length],
         'sepal width (cm)' : [sepal_width],
         'petal length (cm)': [petal_length],
         'petal width (cm)' : [petal_width]  
        }
    )

    # Transform dataset
    data_predict_transf = transformer.transform(data_predict)

    # Make predictions
    predictions = model.predict(data_predict_transf)
    
    return predictions.tolist()