#run with:  uvicorn app:app --reload

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.middleware("http")
async def medify_request_response_middleware(request: Request, call_next):
    request.scope["path"] = str(request.url.path).replace("api", "apiv2")
    response = await call_next(request)
    if isinstance(response, StreamingResponse):
        response.headers["X-Custom-Header"] = "Modified"
    return response

@app.get("/info")
async def hello():
    return {"message":"Hello, World"}

@app.get("/apiv2/info")
async def hellov2():
    
    return {"Message":"Hello, world from V2"}