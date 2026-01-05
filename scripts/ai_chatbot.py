"""
==================================================
 AI CHATBOT - SINGLE FILE PYTHON PROJECT
 Author: You
 Description:
 - Rule-based + NLP style chatbot
 - Intent detection
 - Memory
 - Conversation flow
 - Offline chatbot (no API)
==================================================
"""

import random
import datetime
import json
import os
import re

# -----------------------------
# Utility Functions
# -----------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# -----------------------------
# Chatbot Memory
# -----------------------------

MEMORY_FILE = "chatbot_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"name": None, "chats": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

# -----------------------------
# Intent Definitions
# -----------------------------

INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "responses": [
            "Hello! 😊",
            "Hi there!",
            "Hey! How can I help you?"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye 👋",
            "See you soon!",
            "Take care!"
        ]
    },
    "time": {
        "keywords": ["time"],
        "responses": [
            lambda: f"The current time is {get_time()}"
        ]
    },
    "date": {
        "keywords": ["date"],
        "responses": [
            lambda: f"Today's date is {get_date()}"
        ]
    },
    "name": {
        "keywords": ["my name is", "i am"],
        "responses": [
            "Nice to meet you, {name}!"
        ]
    },
    "feeling": {
        "keywords": ["sad", "happy", "angry", "tired"],
        "responses": [
            "I understand how you feel 💙",
            "Tell me more about it.",
            "I'm here to listen."
        ]
    },
    "unknown": {
        "responses": [
            "I'm not sure I understand.",
            "Can you rephrase that?",
            "Interesting… tell me more."
        ]
    }
}

# -----------------------------
# Intent Detection
# -----------------------------

def detect_intent(user_input):
    for intent, data in INTENTS.items():
        for keyword in data.get("keywords", []):
            if keyword in user_input:
                return intent
    return "unknown"

# -----------------------------
# Response Generator
# -----------------------------

def generate_response(intent, user_input):
    responses = INTENTS[intent]["responses"]
    response = random.choice(responses)

    if callable(response):
        return response()

    if intent == "name":
        name = user_input.split()[-1]
        memory["name"] = name
        save_memory(memory)
        return response.format(name=name)

    return response

# -----------------------------
# Learning Simulation
# -----------------------------

def learn_from_conversation(user_input, bot_response):
    memory["chats"].append({
        "user": user_input,
        "bot": bot_response,
        "time": get_time()
    })
    save_memory(memory)

# -----------------------------
# Main Chat Loop
# -----------------------------

def start_chatbot():
    print("=" * 50)
    print(" 🤖 AI CHATBOT STARTED ")
    print(" Type 'exit' to quit ")
    print("=" * 50)

    if memory["name"]:
        print(f"Welcome back, {memory['name']}! 😊")
    else:
        print("Hello! What's your name?")

    while True:
        user_input = input("\nYou: ")
        cleaned = clean_text(user_input)

        intent = detect_intent(cleaned)
        response = generate_response(intent, cleaned)

        print(f"Bot: {response}")

        learn_from_conversation(user_input, response)

        if intent == "goodbye":
            break

# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    start_chatbot()
