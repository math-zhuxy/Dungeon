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
        self.ai_model = "gpt-3.5-turbo"
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
        self.echos = 1
    def communicate(self, input: str) -> str:
        # 如果是第一轮对话，初始化对话
        if self.echos == 1:
            self.AllMessages.append(
                {
                    "role": "user",
                    "content": "我们开始吧"
                }
            )
        else:
            # 否则，添加用户的输入到对话历史中
            self.AllMessages.append(
                {
                    "role": "user",
                    "content": input
                }
            )
        
        self.echos += 1
        
        # 调用OpenAI API获取回复
        ai_response = self.OpenAI.chat.completions.create(
            model=self.ai_model,
            messages=self.AllMessages
        )
        
        # 提取AI的回复并添加到对话历史中
        assistant_message = ai_response.choices[0].message
        self.AllMessages.append({
            "role": assistant_message.role,
            "content": assistant_message.content
        })
        
        return assistant_message.content
