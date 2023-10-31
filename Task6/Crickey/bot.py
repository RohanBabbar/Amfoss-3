import discord
import responses
# from discord.ext import commands


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE2MjI2NjUwNjQ0NTQ3NTg3MQ.GeEoqD.2Az2ldrSw01xKqEG7wwnijX4KblhBZ4mbgZBA8'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said : "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            if user_message.lower().find('generate') != -1:
                responses.scrape_cricket_scores()
                with open("cricket_scores.csv" , "rb") as file:
                    await message.author.send(file=discord.File(file,"cricket_scores.csv"))
        elif user_message[0] == '/':
            if user_message.lower().find('generate') != -1:
                responses.scrape_cricket_scores()
                with open("cricket_scores.csv" , "rb") as file:
                    await message.channel.send(file=discord.File(file,"cricket_scores.csv"))
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
if __name__ == '__main__':
    run_discord_bot()