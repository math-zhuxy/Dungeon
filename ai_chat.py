import openai

class AIChat:
    def __init__(self):
        MY_API_KEY = "sk-ImhibhfhCvKHSI9y5e5806C924F243E895D8255251FeA4D4"
        OPENAI_URL = "https://api1.zhtec.xyz/v1"
        self.OpenAI = openai.OpenAI(
            api_key = MY_API_KEY, 
            base_url = OPENAI_URL
        )
        self.AllMessages = [
            {
                "role": "system",
                "content": "尽量使用提供的函数，而且可能需要多步函数调用。你不需要知道excel文件的名称或者位置，这个信息是默认的。如果用户没有说明具体的工作表，默认工作表名称为Sheet1。你的输出必须是中文。"
            }
        ]