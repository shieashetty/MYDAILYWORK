def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # ---------- NEGATIVE PHRASES ----------
    negative_phrases = [
        "not good", "dont feel good", "do not feel good",
        "not okay", "dont feel okay", "do not feel okay",
        "not fine", "dont feel fine", "do not feel fine",
        "not feeling well", "dont feel well", "do not feel well"
    ]

    if any(phrase in user_input for phrase in negative_phrases):
        return (
            "I’m really sorry you’re feeling this way.\n"
            "You don’t have to go through it alone.\n"
            "Would you like to talk, try breathing, or get some tips?"
        )

    # ---------- FOLLOW-UP POSITIVE ----------
    elif any(phrase in user_input for phrase in [
        "everything", "all good", "all great",
        "love my life", "life is good", "life is great",
        "going well", "going great"
    ]):
        return (
            "That’s really wonderful to hear.\n"
            "It sounds like things are going well for you.\n"
            "What do you think has helped you feel this way?"
        )

    # ---------- GREETINGS ----------
    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        return (
            "Hello, I’m here to listen.\n"
            "How are you feeling right now?"
        )

    # ---------- EMOTIONAL STATES ----------
    elif any(word in user_input for word in ["sad", "down", "upset", "low"]):
        return (
            "I’m really sorry you’re feeling this way.\n"
            "You don’t have to carry it alone.\n"
            "If you want, you can say: breathe, talk, or tips."
        )

    elif any(word in user_input for word in ["stressed", "anxious", "anxiety", "worried"]):
        return (
            "That sounds overwhelming.\n"
            "Let’s slow things down for a moment.\n"
            "You can try breathing or tell me what’s causing the stress."
        )

    elif any(word in user_input for word in ["tired", "exhausted", "burnt out"]):
        return (
            "Feeling tired can be really heavy.\n"
            "It’s okay to pause.\n"
            "Resting is not being lazy."
        )

    elif "lonely" in user_input:
        return (
            "Feeling lonely can hurt a lot.\n"
            "Even though I’m just a program, I’m here with you.\n"
            "Do you want to talk about what’s making you feel this way?"
        )

    elif any(word in user_input for word in ["overwhelmed", "confused"]):
        return (
            "That’s a lot to handle at once.\n"
            "Sometimes breaking things into small steps helps.\n"
            "What feels the hardest right now?"
        )

    elif any(word in user_input for word in ["angry", "frustrated", "mad"]):
        return (
            "Those feelings are completely valid.\n"
            "Anger often means something important matters to you.\n"
            "Do you want to vent or try something calming?"
        )

    # ---------- POSITIVE STATE ----------
    elif any(word in user_input for word in ["happy", "good", "fine", "okay"]):
        return (
            "I’m really glad to hear that 😊\n"
            "What’s been going well for you?"
        )

    # ---------- ACTION COMMANDS ----------
    elif "breathe" in user_input:
        return (
            "Okay, let’s breathe together.\n"
            "Inhale for 4 seconds…\n"
            "Hold for 4 seconds…\n"
            "Exhale slowly for 6 seconds.\n"
            "Repeat this a few times."
        )

    elif "talk" in user_input:
        return (
            "I’m here to listen.\n"
            "You can share whatever is on your mind."
        )

    elif "tips" in user_input:
        return (
            "Here are a few gentle self-care ideas:\n"
            "- drink some water\n"
            "- stretch your body\n"
            "- write one thought down\n"
            "- take a short break from screens"
        )

    elif any(word in user_input for word in ["help", "menu", "options"]):
        return (
            "You can talk to me about feeling:\n"
            "sad, stressed, tired, lonely, overwhelmed, angry, or happy.\n"
            "You can also say: breathe, talk, tips, or bye."
        )

    # ---------- THANK YOU / CLOSING ----------
    elif any(phrase in user_input for phrase in ["thank", "thanks", "that helped", "helped"]):
        return (
            "I’m really glad I could help 🤍\n"
            "If you ever want to talk, I’ll be right here.\n"
            "You can type 'bye' whenever you want to exit."
        )

    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return (
            "Take care 🤍\n"
            "Be gentle with yourself today."
        )

    # ---------- FALLBACK ----------
    else:
        return (
            "I’m listening.\n"
            "You can tell me more, or type 'options' to see what I understand."
        )
