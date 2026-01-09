# Rule-Based Mental Wellness Support Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello 🤍 I’m here to listen. How are you feeling today?"

    elif "sad" in user_input or "down" in user_input:
        return "I'm sorry you're feeling this way. You're not alone. Would you like a small breathing or grounding exercise?"

    elif "stressed" in user_input or "anxious" in user_input:
        return "That sounds overwhelming. Try taking a slow breath in for 4 seconds, hold for 4, and breathe out for 6."

    elif "tired" in user_input or "exhausted" in user_input:
        return "It’s okay to feel tired. Make sure you’re resting and being kind to yourself today."

    elif "happy" in user_input or "good" in user_input:
        return "I’m really glad to hear that 😊 Keep doing what’s working for you."

    elif "help" in user_input:
        return (
            "I can offer emotional support, calming suggestions, or simple self-care tips. "
            "If you're feeling overwhelmed, talking to someone you trust can really help."
        )

    elif "bye" in user_input or "exit" in user_input:
        return "Take care 🤍 Remember to be gentle with yourself."

    else:
        return (
            "I may not fully understand, but I’m here with you. "
            "Would you like to talk a bit more about how you're feeling?"
        )


# Main program loop
print("🌱 Mental Wellness Support Bot")
print("Note: This chatbot provides general emotional support and is not a medical professional.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)

    if user.lower() in ["bye", "exit"]:
        break
