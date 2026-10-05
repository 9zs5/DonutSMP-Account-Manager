# DonutSMP Account Manager - Setup Guide

## What This Does

When you or your friends install this mod:
- **Automatically** detects when connecting to donutsmp.net
- **Automatically** sends messages to Discord (no setup needed)
- Works with any number of friends
- One Discord bot runs 24/7 to receive commands
- Commands execute in-game: `!run player1 /spawn` → executes on player1's game

## Setup (One Time)

### 1. Create Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it
3. Go to "Bot" tab → "Add Bot"
4. Copy the **TOKEN**
5. Enable "Message Content Intent"

### 2. Add Bot to Server

1. Go to "OAuth2" → "URL Generator"
2. Scopes: `bot`
3. Permissions: `Send Messages`, `Read Messages/View Channels`
4. Open the generated URL and authorize

### 3. Start the Bot (Host It)

The webhook is **already hardcoded** in the mod and bot.

1. Go to `discord-bot` folder
2. Install Python if you don't have it
3. Run: `pip install -r requirements.txt`
4. Create `bot_config.json`:
   ```json
   {
     "bot_token": "PASTE_YOUR_BOT_TOKEN_HERE"
   }
   ```
5. Run: `python bot.py`
6. Keep it running 24/7 (use a hoster like Heroku, Replit, VPS, or leave your PC on)

### 4. Get the Jar File

Build it:
```bash
./gradlew build
```

The jar: `build/libs/donutsmp-account-manager-1.0.0.jar`

Share this jar with your friends.

## For Your Friends

1. **Install Fabric Loader** (if they don't have it)
2. **Download the jar** and put it in `.minecraft/mods/`
3. **Launch Minecraft**
4. **Connect to donutsmp.net**
5. Done! The mod automatically sends to Discord

## Commands (In Discord)

Use `!` prefix:

- `!help` - Show all commands
- `!whoisonline` - See who's connected to donutsmp.net
- `!run everyone /spawn` - Run `/spawn` on all accounts
- `!run player1 /home` - Run `/home` on player1 only
- `!stats everyone` - Request stats from all
- `!stats player1` - Request stats from player1

## What Gets Sent to Discord

- When someone connects: `[playername] has connected to donutsmp.net`
- Commands you run via Discord
- That's it. No passwords, no emails, no secrets.

## Hosting the Bot 24/7

The bot needs to stay online to receive commands. Options:

1. **Replit** (Free): Upload the bot folder, set to run 24/7
2. **Heroku** (Free tier ended, but alternatives exist)
3. **Your PC**: Leave it running with Python
4. **VPS**: Rent a cheap server and run it there
5. **Cloud**: AWS, Google Cloud, etc.

## Build Instructions (For You)

To build the jar yourself:

```bash
git clone https://github.com/9zs5/DonutSMP-Account-Manager
cd DonutSMP-Account-Manager
./gradlew build
```

The jar is at: `build/libs/donutsmp-account-manager-1.0.0.jar`

## Important Notes

- ✓ No config files needed
- ✓ No usernames to set
- ✓ Webhook is built into the jar
- ✓ Works with unlimited friends
- ✓ Only works on donutsmp.net
- ✓ No passwords stored anywhere
- ✓ No account stealing

## Troubleshooting

**Bot won't start:**
- Make sure Python 3.8+ is installed
- Make sure you edited `bot_config.json` with your token
- Make sure the token is correct

**Mod not sending messages:**
- Make sure you're connected to donutsmp.net (not another server)
- Make sure the Discord bot is running
- Check that your webhook URL is correct in the code

**Friends can't connect:**
- Make sure they have Fabric Loader installed
- Make sure they put the jar in `.minecraft/mods/`
- Make sure they're connecting to donutsmp.net
