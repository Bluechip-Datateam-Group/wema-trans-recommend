from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, StreamingResponse
import uuid

transaction_router = APIRouter()


@transaction_router.post("/transaction", status_code=status.HTTP_200_OK)
async def transaction_classify():  # top_n: int = 5
    """
    Classify a transaction
    This method is used to classify a transaction

    :return: Returns the top transaction classes for the input transaction
    """
    # this is a test transaction endpoint to fill with code
    # the response details the top n predicted classes for the transaction
    # you can include the top_n parameter to specify the number of classes to return
    # the response shows the class name and the probability of the class
    # the sum of the probabilities cannot exceed 1
    # the response can be static to top n classes or dynamic to as many classes as sum to a probability of 0.95
    # A request body needs to be created indicative of the data that will be sent to the endpoint.
    transaction_response = {
        "transaction_id": str(uuid.uuid4()),  # replace this with the transaction id from the input data
        "transaction_classes": [{
            "airtime": 0.8,
            "uber": 0.2
        }]
    }
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Transaction classified successfully!", "data": transaction_response})
