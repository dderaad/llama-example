import sys

import ollama # Install Ollama!
from ollama import AsyncClient
import asyncio
"""
REQUIRED:
Download and run setup for
https://ollama.com/download
May require restarting PyCharm
"""
import textwrap
import random
import os

PROMPTS = ["Why is the sky blue? Answer so that a 15 year old (or younger) will understand. Limit your answer to two sentences.",
           "Describe three aquatic creatures. Keep each description to 2 sentences or fewer. Be a little goofy!",
           "You are Barack Ollama (the former president, but also a llama). Introduce yourself in 1 sentence, then deliver a 4 sentence speech about your plans to fix the economy. You can spit a little, but not too much! Make some llama/alpaca themed puns."]

def simple_main():
    """
    First time will take a while.
    This version has no memory, and treats each prompt independently.
    :return:
    """
    print("Welcome to Llama! Talk to Meta's AI assistant, hosted locally on your own machine using ollama!")
    while True:
        user_prompt = input('> ')
        user_prompt = user_prompt if user_prompt else random.choice(PROMPTS)
        """
        If you are using iDtech "Gaming"-class computers, feel free to replace the string "llama2" with "llama3" for a better
        model.
        """
        result = ollama.generate(model='llama2', prompt=user_prompt)
        print(textwrap.fill(result['response'], 100))


SYSTEM_PROMPTS = [
    "You are an AI text adventure game. Describe an area, and provide 2-4 options to proceed.",
    "Explain things to the user like a brilliant scientist speaking to an 8 year old."
]
conversation = []
client = AsyncClient()

def chat_format(role, message):
    return {"role": role,
            "content": message}

def setup():
    global conversation
    system_prompt = random.choice(SYSTEM_PROMPTS) # Modify this if you want reproducible behavior
    conversation.append(chat_format("system", system_prompt))


async def customizable_chatbot():
    global conversation, client
    message = ""

    async for chunk in await client.chat(model="llama2",
                                         messages=conversation,
                                         stream=True):
        token = chunk["message"]["content"]
        print(token, end="", flush=True)

        message += token

    print()

    conversation.append(chat_format("assistant", message))


def main():
    if True: # Change to true for the simpler behavior
        raise NotImplementedError

    setup()
    while True:
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(customizable_chatbot())
        user_input = input("> ")
        conversation.append(chat_format("user", user_input))


if __name__ == "__main__":

    try:
        main()
    except NotImplementedError as e:
        simple_main()
