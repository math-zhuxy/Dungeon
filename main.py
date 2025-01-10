import ai_chat
if __name__ == "__main__":
    client = ai_chat.AIChat()
    while True:
        print("--------------------------------------")
        user_input = input()
        print(client.communicate(user_input))
        print("--------------------------------------")