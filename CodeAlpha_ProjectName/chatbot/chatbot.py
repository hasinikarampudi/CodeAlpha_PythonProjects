def get_bot_response(user_message):
    user_message = user_message.lower().strip()

    if user_message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif user_message in ["how are you", "how are you?"]:
        return "I'm fine, thanks for asking!"

    elif user_message in ["what is your name", "what's your name"]:
        return "I am a simple Python chatbot."

    elif user_message in ["help", "what can you do"]:
        return "I can respond to greetings, answer how I am, and say goodbye."

    elif user_message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I did not understand that. Please try again."


def start_chatbot():
    print("Welcome to the Basic Chatbot!")
    print("Type 'bye' or 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")
        response = get_bot_response(user_message)
        print("Bot:", response)

        if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    start_chatbot()