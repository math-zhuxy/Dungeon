from tempfile import template
import fastapi.staticfiles
import fastapi.templating
import pydantic
import fastapi
import ai_chat

class Item(pydantic.BaseModel):
    code: str
    msg: str

class Server:
    def __init__(self):
        self.app = fastapi.FastAPI()
        self.app.mount("/static", fastapi.staticfiles.StaticFiles(directory="public/static"), name="static")
        template = fastapi.templating.Jinja2Templates(directory="public")
        self.chat_model = ai_chat.AIChat()

        @self.app.get("/")
        async def index(request: fastapi.Request):
            return template.TemplateResponse("main.html", {"request": request})

        @self.app.get("/ai_chat")
        async def process_message(input: Item):
            return self.chat_model.communicate(input.msg)
        
        @self.app.get("/test")
        async def test(): 
            return {"message": "connection successful"}   
    