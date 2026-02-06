from openai import OpenAI
from pydantic import BaseModel
import json


# refine prompt s.t. it only creates flashcards for RELEVANT concepts and definitions
INSTRUCTION_PROMPT = """
You are an expert tutor that is specialized in assisting students with last minute studying.
Given the parsed text of a slideshow, identify crucial key terms/definitions and generate
key value pairs such that the key is the prompt of a flashcard and the value is the answer
to the flashcard.
""" 

class Card(BaseModel):
    prompt: str
    answer: str

class CardList(BaseModel):
    cards: list[Card] 

client = OpenAI()

async def generate_flash_cards(parsed_text: str) -> json:
    response = client.responses.parse(
        model="gpt-5-nano",
        instructions=INSTRUCTION_PROMPT,
        input=parsed_text,
        text_format=CardList
    )

    card_list_json = response.output[1].content[0].text
    return card_list_json
