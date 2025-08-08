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

PROMPTS = ["Why is the sky blue? Answer so that a 15 year old (or younger) will understand. Limit your answer to two sentences.",
           "Describe three aquatic creatures. Keep each description to 2 sentences or fewer. Be a little goofy!",
           "You are Barack Ollama (the former president, but also a llama). Introduce yourself, then deliver a 4 sentence speech about your plans to fix the economy. You can spit a little, but not too much! Make some wool/llama/alpaca themed puns."]

def simple_main():
    """
    First time will take a while.
    This version has no memory, and treats each prompt independently.
    :return:
    """
    print("Welcome to Llama! Talk to Meta's AI assistant, hosted locally on your own machine!")
    while True:
        user_prompt = input('> ')
        user_prompt = user_prompt if user_prompt else random.choice(PROMPTS)
        """
        If you are using iDtech "Gaming"-class computers, feel free to replace the string "llama2" with "llama3" for a better
        model.
        """
        result = ollama.generate(model='llama2', prompt=user_prompt)
        print(textwrap.fill(result['response'], 100))

if __name__ == "__main__":
    simple_main()