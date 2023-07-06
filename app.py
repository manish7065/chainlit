import chainlit as cl
import os,sys


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...


    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()
