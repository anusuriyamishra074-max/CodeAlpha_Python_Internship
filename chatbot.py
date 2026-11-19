def chatbot():

    print("Welcome to Python Chatbot!")
    print("Type 'bye' to exit.")

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I am fine, thank you!")

        elif user == "what is your name":
            print("Bot: I am Python Chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()