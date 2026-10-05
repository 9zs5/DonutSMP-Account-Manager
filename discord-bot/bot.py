#!/usr/bin/env python3
"""
DonutSMP Account Manager Discord Bot
- No password storage
- No account theft
- Only reports usernames and server status
- Commands: !help, !whoisonline, !run, !stats
- Prefix: !
"""

import discord
from discord.ext import commands
import json
import os

# Hardcoded webhook URL (same as in mod)
WEBHOOK_URL = "https://discord.com/api/webhooks/1556402645080473821/m-RyTFEFUF1a4HSaRfxOd54UHt-tSTVhJA_3HVwleGtgqjylKp9zRibibbHyqkG_cJ8x"

# Config file
CONFIG_FILE = 'bot_config.json'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"[DonutSMP] Creating {CONFIG_FILE}...")
        config = {
            "bot_token": "PASTE_YOUR_BOT_TOKEN_HERE"
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"[DonutSMP] Please edit {CONFIG_FILE} with your Discord bot token")
        print("[DonutSMP] Get your token from: https://discord.com/developers/applications")
        exit(1)
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

config = load_config()
BOT_TOKEN = config['bot_token']

# Discord bot setup with ! prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'[DonutSMP] ✓ Bot logged in as {bot.user}')
    print(f'[DonutSMP] ✓ Webhook URL: Hardcoded')
    print(f'[DonutSMP] ✓ Prefix: !')
    await bot.change_presence(activity=discord.Game(name="!help for commands"))

@bot.command(name='help')
async def help_command(ctx):
    """Show all available commands"""
    embed = discord.Embed(title="DonutSMP Account Manager", color=discord.Color.blue())
    embed.add_field(name="!help", value="Show this message", inline=False)
    embed.add_field(name="!whoisonline", value="Show who is online on donutsmp.net", inline=False)
    embed.add_field(name="!run everyone <command>", value="Run command on all accounts", inline=False)
    embed.add_field(name="!run <username> <command>", value="Run command on specific account", inline=False)
    embed.add_field(name="!stats everyone", value="Get stats from all accounts", inline=False)
    embed.add_field(name="!stats <username>", value="Get stats from specific account", inline=False)
    embed.add_field(name="Examples:", value="!run player1 /spawn\n!run everyone /home\n!stats player1", inline=False)
    embed.set_footer(text="Note: No passwords stored. Only usernames and server status tracked.")
    await ctx.send(embed=embed)

@bot.command(name='whoisonline')
async def who_is_online(ctx):
    """Check who is online on donutsmp.net"""
    embed = discord.Embed(title="Online Players on donutsmp.net", color=discord.Color.green())
    embed.description = "Players will appear here when they connect to donutsmp.net\nThe mod automatically reports connections."
    await ctx.send(embed=embed)

@bot.command(name='run')
async def run_command(ctx, target: str, *, command: str):
    """Run a command on accounts"""
    if not command:
        await ctx.send("❌ Please provide a command")
        return
    
    if target.lower() == "everyone":
        embed = discord.Embed(
            title="Running command on ALL accounts",
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
    """Get stats from accounts"""
    if target.lower() == "everyone":
        embed = discord.Embed(
            title="Getting stats from ALL accounts",
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
        await ctx.send(f"❌ Missing argument: {error.param.name}\nType `!help` for usage")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Unknown command. Type `!help` for available commands")
    else:
        await ctx.send(f"❌ Error: {str(error)}")

# Run bot
print("[DonutSMP] Starting Account Manager bot...")
print("[DonutSMP] Webhook: Hardcoded")
print("[DonutSMP] Prefix: !")
try:
    bot.run(BOT_TOKEN)
except discord.errors.LoginFailure:
    print("[DonutSMP] ❌ Invalid bot token!")
    print(f"[DonutSMP] Please check your bot token in {CONFIG_FILE}")
except Exception as e:
    print(f"[DonutSMP] ❌ Error: {e}")