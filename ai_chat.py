import openai
import utils

class AIChat:
    def __init__(self):
        MY_API_KEY = "sk-ImhibhfhCvKHSI9y5e5806C924F243E895D8255251FeA4D4"
        OPENAI_URL = "https://api1.zhtec.xyz/v1"
        self.OpenAI = openai.OpenAI(
            api_key = MY_API_KEY, 
            base_url = OPENAI_URL
        )
        try:
            with open(file = "prompt.md", mode = 'r', encoding = 'utf-8') as file:
                BASE_PROMPT = file.read()
        except FileNotFoundError:
            print(f"文件 prompt.md 未找到。")
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
        self.AllMessages = [
            {
                "role": "system",
                "content": BASE_PROMPT
            }
        ]