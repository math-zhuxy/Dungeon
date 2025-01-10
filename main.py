import ai_chat
if __name__ == "__main__":
    client = ai_chat.AIChat()
    print("按下回车健开始游戏")
    while True:
        print("--------------------------------------")
        user_input = input()
        print(client.communicate(user_input))
        print("")