import chainlit as cl
import os,sys



OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
import os
import json
from src.llm import messages,get_gpt_response

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...
    messages.append({'role':'user','content':message})
    print(f">>>>Messages to gpt: {messages}")
    chat_response = get_gpt_response(messages)
    print(f">>>>Chat Reaponse: {chat_response}")
    messages.append({'role':'assistant','content':chat_response})

    # Send a response back to the user
    await cl.Message(
        content=chat_response
    ).send()
