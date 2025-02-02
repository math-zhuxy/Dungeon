import openai
import json
class AIChat:
    def __init__(self):
        try:
            with open(file= "config.json", mode='r', encoding='utf-8') as file:
                config = json.load(file)
                MY_API_KEY = config["api_key"]
                OPENAI_URL = config["base_url"]
        except FileNotFoundError:
            print(f"文件 config.json 未找到。")
        except KeyError as e:
            print(f"配置文件缺少键: {e}")
        except Exception as e: 
            print(f"未知错误: {e}")

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
            print(f"未知错误: {e}")
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

        # 捕捉错误
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
        
        if not ai_response.choices:
            return "AI没有回复。"

        # 提取AI的回复并添加到对话历史中
        assistant_message = ai_response.choices[0].message
        self.AllMessages.append({
            "role": assistant_message.role,
            "content": assistant_message.content
        })
        
        return assistant_message.content