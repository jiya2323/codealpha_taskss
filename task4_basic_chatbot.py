# Task 4: Basic Chatbot

def chatbot():
    print("Chatbot is running! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!\n")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!\n")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: I didn't understand that. Try: hello, how are you, bye\n")


chatbot()