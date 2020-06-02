import discord
import requests

TOKEN = "NzA5NzAzNTgwNzIxODcyODk2.XrpyDA.WUjTDTnD8zoxAKabhFQ9wJQHvEg"

CLIENT = discord.Client()


async def reduser(message: discord.Message):
    cat = "https://api.thecatapi.com/v1/images/search"
    dog = "https://dog.ceo/api/breeds/image/random"
    text = message.content.lower()
    if "кот" in text or "кошк" in text:
        response = requests.get(cat)
        await message.channel.send(response.json()[0].get('url'))
    elif "пёс" in text or "собак" in text:
        response = requests.get(dog)
        await message.channel.send(response.json().get("message"))


@CLIENT.event
async def on_ready():
    print(f'{CLIENT.user} подключен к Discord!')
    for guild in CLIENT.guilds:
        print(
            f'{CLIENT.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})'
        )


@CLIENT.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    await reduser(message)


def main():
    CLIENT.run(TOKEN)


if __name__ == "__main__":
    main()
