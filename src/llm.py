import os
import openai
from src.prompts import system_instruction

messages = [{'role':'system','content':system_instruction}]

def get_gpt_response(messages,model="gpt-3.5-turbo",temperature=0):
    try:
        response=openai.ChatCompletion.create(
            model=model,
            temperature=temperature,
            messages=messages
        )
        return response.choices[0].message["content"]
        
    except Exception as e:
        print(f"Error occured in zomato bot: {e}")
        raise e
