import discord
from discord.ext import commands
import requests
import os

DISCORD_TOKEN = os.environ["MTQ4OTczMzA3MDkyMjg0MjI3Mg.GVmD_R.UzuadprapZkUumVZKL8LuM133-8z9VYG_WlBA4"]
OPENROUTER_API_KEY = os.environ["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"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except:
        return "Błąd AI 😅"

@bot.event
async def on_ready():
    print(f"Bot działa jako {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # chatbot odpowiada na wiadomości
    user_input = message.content

    reply = ask_ai(user_input)

    await message.channel.send(f"{message.author.mention} {reply}")

    await bot.process_commands(message)

bot.run(MTQ4OTczMzA3MDkyMjg0MjI3Mg.GVmD_R.UzuadprapZkUumVZKL8LuM133-8z9VYG_WlBA4)