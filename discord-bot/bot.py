#!/usr/bin/env python3
import discord
from discord.ext import commands
import json
import os

# Config file
CONFIG_FILE = 'bot_config.json'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"Creating {CONFIG_FILE}...")
        config = {
            "bot_token": "PASTE_YOUR_BOT_TOKEN_HERE",
            "webhook_url": "PASTE_YOUR_WEBHOOK_URL_HERE"
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Please edit {CONFIG_FILE} with your bot token and webhook URL")
        exit(1)
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

config = load_config()
BOT_TOKEN = config['bot_token']
WEBHOOK_URL = config['webhook_url']

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✓ Bot logged in as {bot.user}')
    print(f'✓ Using single webhook for all accounts')
    await bot.change_presence(activity=discord.Game(name="/help for commands"))

@bot.command(name='help')
async def help_command(ctx):
    embed = discord.Embed(title="DonutSMP Account Manager", color=discord.Color.blue())
    embed.add_field(name="/help", value="Show this message", inline=False)
    embed.add_field(name="/whoisonline", value="Show online players", inline=False)
    embed.add_field(name="/run everyone <command>", value="Run command on all accounts", inline=False)
    embed.add_field(name="/run <account> <command>", value="Run command on one account", inline=False)
    embed.add_field(name="/stats everyone", value="Get stats for all accounts", inline=False)
    embed.add_field(name="/stats <account>", value="Get stats for one account", inline=False)
    embed.add_field(name="Example:", value="/run Account1 /spawn\n/stats Account2", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='whoisonline')
async def who_is_online(ctx):
    embed = discord.Embed(title="Checking online players...", color=discord.Color.green())
    embed.description = "Your mods will report who is online on donutsmp.net"
    await ctx.send(embed=embed)

@bot.command(name='run')
async def run_command(ctx, target: str, *, command: str):
    """Run a command on your accounts"""
    if target.lower() == "everyone":
        embed = discord.Embed(
            title="Running command on all accounts",
            description=f"Command: `{command}`",
            color=discord.Color.orange()
        )
    else:
        embed = discord.Embed(
            title=f"Running command on {target}",
            description=f"Command: `{command}`",
            color=discord.Color.orange()
        )
    
    await ctx.send(embed=embed)

@bot.command(name='stats')
async def stats_command(ctx, target: str):
    """Get stats from your accounts"""
    if target.lower() == "everyone":
        embed = discord.Embed(
            title="Getting stats from all accounts",
            color=discord.Color.purple()
        )
    else:
        embed = discord.Embed(
            title=f"Getting stats from {target}",
            color=discord.Color.purple()
        )
    
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing argument: {error.param.name}\nType `/help` for usage")
    else:
        await ctx.send(f"❌ Error: {str(error)}")

# Run bot
print("Starting DonutSMP Account Manager bot...")
try:
    bot.run(BOT_TOKEN)
except discord.errors.LoginFailure:
    print("❌ Invalid bot token!")
    print(f"Please check your bot token in {CONFIG_FILE}")
except Exception as e:
    print(f"❌ Error: {e}")
