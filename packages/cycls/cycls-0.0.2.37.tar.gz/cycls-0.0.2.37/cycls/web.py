import json, inspect

async def openai_encoder(stream): # clean up the meta data / new API?
    async for message in stream:
        payload = {"id": "chatcmpl-123",
                   "object": "chat.completion.chunk",
                   "created": 1728083325,
                   "model": "model-1-2025-01-01",
                   "system_fingerprint": "fp_123456",
                   "choices": [{"delta": {"content": message}}]}
        if message:
            yield f"data: {json.dumps(payload)}\n\n"
    yield "data: [DONE]\n\n"

test_auth_public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyDudrDtQ5irw6hPWf2rw
FvNAFWeOouOO3XNWVQrjXCZfegiLYkL4cJdm4eqIuMdFHGnXU+gWT5P0EkLIkbtE
zpqDb5Wp27WpSRb5lqJehpU7FE+oQuovCwR9m5gYXP5rfM+CQ7ZPw/CcOQPtOB5G
0UijBhmYqws3SFp1Rk1uFed1F/esspt6Ifq2uDSHESleylqTKUCQiBa++z4wllcV
PbNiooLRpsF0kGljP2dXXy/ViF7q9Cblgl+FdrqtGfHD+DHJuOSYcPnRa0IHZYS4
r5i9C2lejVrEDqgJk5IbmQgez0wmEG4ynAxiDLvfdtvrd27PyBI75FsyLER/ydBH
WwIDAQAB
-----END PUBLIC KEY-----
"""

live_auth_public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAorfL7XyxrLG/X+Kq9ImY
oSQ+Y3PY5qi8t8R4urY9u4ADJ48j9LkmFz8ALbubQkl3IByDDuVbka49m8id9isy
F9ZJErsZzzlYztrgI5Sg4R6OJXcNWLqh/tzutMWJFOrE3LnHXpeyQMo/6qAd59Dx
sNqzGxBTGPV1BZvpfhp/TT/sjgbPQWHS4PMpKD4vZLKXeTNJ913fMTUoFAIaL0sT
EhoeLUwvIuhLx4UYTmjO/sa+fS6mdghjddOkjSS/AWr/K8mN3IXDImGqh83L7/P0
RCru4Hvarm0qPIhfwEFfWhKFXONMj3x2fT4MM1Uw1H7qKTER2MtOjmdchKNX7x9b
XwIDAQAB
-----END PUBLIC KEY-----
"""

def web(func, front_end_path="", prod=False, org=None, api_token=None, header="", intro="", auth=True): # API auth
    from fastapi import FastAPI, Request, HTTPException, status, Depends
    from fastapi.responses import StreamingResponse , HTMLResponse
    from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
    import jwt
    from pydantic import BaseModel, EmailStr
    from typing import List, Optional
    from fastapi.templating import Jinja2Templates
    from fastapi.staticfiles import StaticFiles

    class User(BaseModel):
        id: str
        name: str
        email: EmailStr
        org: Optional[str] = None
        plans: List[str] = []

    class Context(BaseModel):
        messages: List[dict]
        user: Optional[User] = None

    app = FastAPI()
    bearer_scheme = HTTPBearer()

    def validate(bearer: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
        # if api_token and api_token==""
        try:
            public_key = live_auth_public_key if prod else test_auth_public_key
            decoded = jwt.decode(bearer.credentials, public_key, algorithms=["RS256"])
            # print(decoded)
            return {"type": "user", 
                    "user": {"id": decoded.get("id"), "name": decoded.get("name"), "email": decoded.get("email"), "org": decoded.get("org"),
                             "plans": decoded.get("public").get("plans", [])}}
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
    
    @app.post("/")
    @app.post("/chat/completions")
    async def back(request: Request, jwt: Optional[dict] = Depends(validate) if auth else None):
        data = await request.json()
        messages = data.get("messages")
        user_data = jwt.get("user") if jwt else None
        context = Context(messages = messages, user = User(**user_data) if user_data else None)
        stream = await func(context) if inspect.iscoroutinefunction(func) else func(context)
        if request.url.path == "/chat/completions":
            stream = openai_encoder(stream)
        return StreamingResponse(stream, media_type="text/event-stream")

    templates = Jinja2Templates(directory=front_end_path)
    @app.get("/", response_class=HTMLResponse)
    async def front(request: Request):
        return templates.TemplateResponse("index.html", {
                "request": request, "header": header, "intro": intro, "prod": prod, "auth": auth, "org": org,
                "pk_live": "pk_live_Y2xlcmsuY3ljbHMuY29tJA", "pk_test": "pk_test_c2VsZWN0LXNsb3RoLTU4LmNsZXJrLmFjY291bnRzLmRldiQ"
            })
    app.mount("/", StaticFiles(directory=front_end_path, html=False))
    return app