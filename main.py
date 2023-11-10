from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query
import pickle
from pydantic import BaseModel

from app.views.transaction_views import transaction_router

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

app = FastAPI(openapi_url="/openapi.json",title="Transaction classification service",version="V1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


class PredictionInput(BaseModel):
    narration: str

def load_object(filename): 
    with open(filename, "rb") as file:
        loaded_object = pickle.load(file)
    return loaded_object

def predict_category(narration: str) -> str:
    model = load_object("svm_model.p")
    return model.predict([narration])[0]


##try out how to use this for multiple features
@app.get("/predict")
def predict(narration: str = Query(default=None, description="text Narration")):
    if narration is None:
        return {"error": "Please provide the 'text Narration' parameter."}
    
    result = predict_category(narration)
    return {"prediction": result}

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Assuming predict_category is your function for making predictions
        # Modify this according to your actual prediction logic
        result = predict_category(input_data.narration)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
app.include_router(transaction_router, tags=["Transaction Classification"], prefix="/api/v1")
