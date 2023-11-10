# from config import auth_code
# from fastapi import Request, HTTPException, status
#
#
# async def verify_token(req: Request):
#     token = req.headers['Authorization']
#     if token != auth_code:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail={"message": "Unauthorized", "success": False,
#                                     "reason": "Authorization token is invalid",
#                                     "data":{}})
#     return True
