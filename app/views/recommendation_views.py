from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, StreamingResponse
import uuid

recommendation_router = APIRouter()


@recommendation_router.post("/recommend", status_code=status.HTTP_200_OK)
async def product_recommend():  # top_n: int = 5
    """
    Recommend a product
    This method is used to recommend a product

    :return: Returns the top transaction classes for the input transaction
    """
    # this is a test transaction endpoint to fill with code
    # the response details the top n predicted classes for the transaction
    # you can include the top_n parameter to specify the number of classes to return
    # the response shows the class name and the probability of the class
    # the sum of the probabilities cannot exceed 1
    # the response can be static to top n classes or dynamic to as many classes as sum to a probability of 0.95
    # A request body needs to be created indicative of the data that will be sent to the endpoint.
    recommendation_response = {
        "recommendations": [{
            "airtime": 0.8,
            "uber": 0.2
        }]
    }
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Recommendation successful!", "data": recommendation_response})
