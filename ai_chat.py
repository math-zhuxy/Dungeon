import openai
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
    def communicate(self, input: str) ->str:
        self.AllMessages.append(
            {
                "role": "user",
                "content": input
            }
        )
        self.echos += 1
        try:
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

        except openai.AuthenticationError as e:
            return f"API密钥错误: {e}"
        except openai.BadRequestError as e:
            return f"请求错误：{e}"
        except openai.ContentFilterFinishReasonError as e: 
            return f"内容过滤错误：{e}"
        except openai.InternalServerError as e:
            return f"服务器错误: {e}"
        except openai.APITimeoutError as e:
            return f"API超时错误: {e}"
        except Exception as e:
            return f"未知错误: {e}"
        
        return assistant_message.content