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

def simple_main():
    """
    First time will take a while
    :return:
    """
    print("Welcome to Llama! Talk to Meta's AI assistant, hosted locally on your own machine!")
    while True:
        user_prompt = input('> ')
        user_prompt = user_prompt if user_prompt else "Why is the sky blue? Limit your answer to two sentences."
        """
        If you are using iDtech "Gaming"-class computers, feel free to replace the string "llama2" with "llama3" for a better
        model.
        """
        result = ollama.generate(model='llama2', prompt=user_prompt)
        print(textwrap.fill(result['response'], 80))

if __name__ == "__main__":
    simple_main()