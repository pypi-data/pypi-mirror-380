import logging

from discord import Intents

from zns_discord_bot.zns_discord_bot import ZnsDiscordBot

bot = ZnsDiscordBot(
    token="MTQyMDYxNzQwMTczNjc2MTM4NA.GeJJ-7.bxu-Kiv3rsqw5Ag3toH2KLs7NTeiBYzQVlB-Ig",
    command_prefix="!",
    intents=Intents.all(),
    use_easy_embed=True,
    use_bot_colour=True,
    log_level=logging.INFO,
    colour=int("FF0000", 16),
    log_file_path_bot="logs/bot.log",
    log_file_path_sys="logs/system.log"
)

@bot.command()
async def hello(ctx):
    await bot.send_info(ctx, "Hello, world!")

@bot.command()
async def ping(ctx):
    await bot.send_debug(ctx, f"Pong! Latency: {round(bot.latency * 1000)}ms")

@bot.command()
async def bye(ctx):
    await bot.reply_warning(ctx, "Goodbye, world!", mention_author=True)

bot.init()
