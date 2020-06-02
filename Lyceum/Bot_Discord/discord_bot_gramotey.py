import discord
import requests
import time

TOKEN = "NzA4MzM5MTM0NDA1NTQxOTQ5.XrkNmg.ZuumfyF98TmrxJVySKVycP0Sg5M"

CLIENT = discord.Client()


@CLIENT.event
async def reduser(message: discord.Message):
    text = message.content
    if "set_timer" in text:
        t = text.split()
        h = int(t[2])
        m = int(t[4])
        s = (h * 360) + (m*60)
        await message.channel.send(f"у тебя {h} часов {m} минут")
        time.sleep(s)
        await message.channel.send("время вышло")


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
