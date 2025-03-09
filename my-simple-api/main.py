from fastapi import FastAPI
import random

app = FastAPI()

# we will build two different endpoints
# side_hustles
# money_quotes

side_hustle = [
    "Freelancing -> Sell your services and goods",
    "Youtube -> Make your unique content to earn money",
    "Amazon -> Sell physical products and let Amazon handle storage, shipping, and customer service.",
    "Etsy -> Sell handmade or vintage items, craft supplies, or digital products (e.g., printable planners, art, or designs).",
    "Shopify -> Build an online store to sell products directly to customers.",
    "Niche Website -> Create a blog or website focused on a specific topic (e.g., personal finance, travel, health).",
    "Sell on Instagram -> Use Instagram to promote products, either your own or as an affiliate.",
    "Online Courses -> Create and sell courses on platforms like Udemy, Teachable, or Skillshare.",
    "Dropshipping -> Start an online store without holding inventory. Partner with suppliers who ship products directly to customers.",
    "Stock Photography -> Sell your photos on platforms like Shutterstock, Adobe Stock, or Getty Images.",
    "Podcasting -> Start a podcast and monetize through sponsorships, ads, or listener donations.",
    "Virtual Assistant -> Offer administrative, technical, or creative assistance to businesses or entrepreneurs remotely."
]

money_quotes = [
    "The best way to predict the future is to invent it.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "Money is like gasoline during a road trip. You don't want to run out of gas on your way there.",
    "Money is like a sixth sense. Everybody has it, but few people know how to use it.",
    "The way to get started is to quit talking and begin doing.",
    "The only thing worse than starting something and failing... is not starting something.",
    "Money grows on trees, but you have to climb them first.",
]

@app.get("/side_hustle")
def get_side_hustle(apiKey: str):
    """Returns a random side hustle idea"""
    if apiKey != "123456":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustle)}

@app.get("/money_quotes")
def get_money_qoutes(apiKey: str):
    """Returns a random money qoutes"""
    if apiKey != "123456":
        return {"error": "Invalid API key"}
    return {"money_qoutes": random.choice(money_quotes)} 