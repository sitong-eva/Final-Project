import requests
import json

url='https://tarot-api.onrender.com/api/v1/cards'
response = requests.get(url)

data=json.loads(response.text)
# print(data)

cards=data['cards']
# print(cards)

#List of Cards
lst=[]

for card in cards:
    print(card)
    lst.append(card['name'])
print(lst)

def draw_love():
    """
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fvekkesind.com%2Ftarot-spreads-for-love%2F&psig=AOvVaw1R0lUvivsd1N6vmbr8Xr8n&ust=1682457158030000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDLnLy3w_4CFQAAAAAdAAAAABAd
    """
    pass

def draw_yearly_forecast():
    """
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fmywanderingfool.com%2Ftarot%2Ftarot%2Fhow-to-map-out-the-year-ahead-a-new-years-tarot-spread%2F&psig=AOvVaw1FtbMLSaCV9MYNrsBDsoyx&ust=1682457244279000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOimmOW3w_4CFQAAAAAdAAAAABAY 
    """
    pass
    
def draw_career():

def draw_education():

def draw_

