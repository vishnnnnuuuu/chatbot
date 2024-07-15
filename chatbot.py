import random

def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    responses = {
        "hi": ["Hello!", "Hi there!", "Greetings!"],
        "how are you?": ["I'm just a program, but thanks for asking!", "Doing well, how about you?"],
        "what is your name?": ["I'm a chatbot created by you!", "I don't have a name, but you can call me Chatbot."],
        "bye": ["Goodbye!", "See you later!", "Take care!"]
    }

    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Check if the user input matches any key in the responses
        response = responses.get(user_input, ["Sorry, I don't understand that."])
        print("Chatbot:", random.choice(response))

if __name__ == "__main__":
    chatbot()
