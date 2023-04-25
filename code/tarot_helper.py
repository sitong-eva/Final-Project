import requests
import json
import random
import os
import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY
# Tarot API
url = "https://tarot-api.onrender.com/api/v1/cards"
response = requests.get(url)

data = json.loads(response.text)
# print(data)

cards = data["cards"]
# print(cards)

# List of Cards
lst = []

for card in cards:
    # print(card)
    lst.append(card["name"])
# print(lst)


def draw_love():
    """
    This function draws tarots cards from Lst, to get a tarot spread to predict love.
    Returns 3 cards, for past, present, and future for love life of user.
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fvekkesind.com%2Ftarot-spreads-for-love%2F&psig=AOvVaw1R0lUvivsd1N6vmbr8Xr8n&ust=1682457158030000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDLnLy3w_4CFQAAAAAdAAAAABAd
    """
    love_past = random.choice(lst)
    love_present = random.choice(lst)
    love_future = random.choice(lst)
    love = love_past, love_present, love_future
    return love


def draw_yearly_forecast():
    """
    This function draws tarots cards from Lst, to get a tarot spread to predict the yearly forecast.
    Returns 7 cards, for main theme, departing energies, talents, future opportunities, obstacles, dealing with obstacles, and achievements for the yearly forecase of user
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fmywanderingfool.com%2Ftarot%2Ftarot%2Fhow-to-map-out-the-year-ahead-a-new-years-tarot-spread%2F&psig=AOvVaw1FtbMLSaCV9MYNrsBDsoyx&ust=1682457244279000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOimmOW3w_4CFQAAAAAdAAAAABAY
    """
    yearly_main_theme = random.choices(lst)
    yearly_departing_energies = random.choices(lst)
    yearly_talents = random.choices(lst)
    yearly_future_opportunities = random.choices(lst)
    yearly_obstacles = random.choices(lst)
    yearly_obstacles_deal = random.choices(lst)
    yearly_achieve = random.choices(lst)
    yearly = (
        yearly_main_theme,
        yearly_departing_energies,
        yearly_talents,
        yearly_future_opportunities,
        yearly_obstacles,
        yearly_obstacles_deal,
        yearly_achieve,
    )
    return yearly


def draw_career():
    """
    This function draws tarots cards from Lst, to get a tarot spread to predict career.
    Returns 3 cards, for stay/leave, new opportunity, and advice for career of user.
    https://mywanderingfool.com/tarot/tarot/best-tarot-card-spreads-career-finances/
    """
    career_stay_leave = random.choice(lst)
    career_new_oopportunity = random.choice(lst)
    career_advice = random.choice(lst)
    career = career_stay_leave, career_new_oopportunity, career_advice
    return career


def draw_general():
    """
    https://preview.redd.it/w40oounkrla41.jpg?auto=webp&s=a55784d2df3029d5efe4e6ceea2fd1b295e4f6b3
    """
    general_as_is = random.choices(lst)
    general_correct_path = random.choices(lst)
    general_main_obstacle = random.choices(lst)
    general_help = random.choices(lst)
    general_progress = random.choices(lst)
    general = (
        general_as_is,
        general_correct_path,
        general_main_obstacle,
        general_help,
        general_progress,
    )
    return general

def answer(type):
    if type == "love":
        tarot = draw_love()
        print(tarot)
        prompt = f"Act as if you are a tarot card reader. Provide a reading on a song about {type}. The tarot spread goes like this: the first card represents the past, the second represents the present, and the third represents the future. I drew these cards from the deck: {tarot}. Please provide concise and complete sentences to interpret the cards for {type}."
        # response from ChatGPT
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.4,
        )
        assistant_reply = response.choices[0].text.strip()
        print("Assistant's interpretation:")
        print(assistant_reply)

    """
    From Text Analysis Project:

    model_engine = "davinci"
    temperature = 0.5
    max_tokens = 50
    stop_sequence = "."

    prompt = f"Act as if you are {musician}, and you're writing a song. What's a line from your song?:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    sentence = response.choices[0].text.strip()
    return sentence
    """

def main():
    # print(draw_love())
    # print(draw_yearly_forecast())
    # print(draw_career())
    # print(draw_general())

    answer("love")


if __name__ == "__main__":
    main()
