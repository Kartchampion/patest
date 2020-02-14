import discord

from time import sleep

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready. Beginning processes in 3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Bot is now active.")


@client.event
async def on_message(message: discord.Message):
    if message.author.id == client.user.id:
        return
    if message.author.name == "Kartchampion":
        await message.channel.send("This is a test.")
        print("Sent a message")
        return
    print("Registered a message.")


def main():
    t = input("Please enter the Bot token: ")
    client.run(t)


if __name__ == '__main__':
    main()
