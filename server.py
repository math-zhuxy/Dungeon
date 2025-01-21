import pydantic
import fastapi
import ai_chat

class Item(pydantic.BaseModel):
    code: str
    msg: str

class Server:
    def __init__(self):
        self.app = fastapi.FastAPI()
        self.chat_model = ai_chat.AIChat()
        @self.app.get("/ai_chat")
        async def process_message(input: Item):
            return self.chat_model.communicate(input.msg)
        
        @self.app.get("/test")
        async def test(): 
            return {"message": "connection successful"}   
    