# Quick Start - DonutSMP Account Manager

## One Time Setup

### 1. Create Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application" → "DonutSMP Manager"
3. Go to "Bot" tab → "Add Bot"
4. Copy the **TOKEN** (save it)
5. Enable "Message Content Intent"

### 2. Add Bot to Your Server

1. Go to "OAuth2" → "URL Generator"
2. Scopes: `bot`
3. Permissions: `Send Messages`, `Read Messages/View Channels`
4. Open the generated URL and add to your server

### 3. Create ONE Webhook

1. Right-click your Discord channel
2. "Edit Channel" → "Integrations" → "Webhooks"
3. "New Webhook" → Name it "DonutSMP"
4. Copy the **Webhook URL**

### 4. Get the Mod Jar

Build it:
```bash
./gradlew build
```

The jar is at: `build/libs/donutsmp-account-manager-1.0.0.jar`

## Install on PC1

1. Put jar in `.minecraft/mods/`
2. Launch Minecraft once
3. Close Minecraft
4. Edit `.minecraft/config/donutsmp-account-manager/config.json`:
   ```json
   {
     "webhook_url": "PASTE_YOUR_WEBHOOK_URL_HERE",
     "account_name": "Account1"
   }
   ```
5. Save

## Install on PC2

1. Put **same jar** in `.minecraft/mods/`
2. Launch Minecraft once
3. Close Minecraft
4. Edit `.minecraft/config/donutsmp-account-manager/config.json`:
   ```json
   {
     "webhook_url": "PASTE_YOUR_WEBHOOK_URL_HERE",
     "account_name": "Account2"
   }
   ```
5. Save (same webhook URL, different account name)

## Run the Discord Bot

1. Make sure Python is installed
2. Go to `discord-bot` folder
3. Run: `pip install -r requirements.txt`
4. Edit `bot_config.json`:
   ```json
   {
     "bot_token": "PASTE_YOUR_BOT_TOKEN_HERE",
     "webhook_url": "PASTE_YOUR_WEBHOOK_URL_HERE"
   }
   ```
5. Run: `python bot.py`

## Test

1. Launch Minecraft on PC1, connect to donutsmp.net
2. Check Discord - you see: `[Account1] Account1 has connected to donutsmp.net`
3. Type `/whoisonline` in Discord
4. Bot responds

## Commands

- `/help` - Show all commands
- `/whoisonline` - See who's online
- `/run Account1 /spawn` - Run on Account1
- `/run everyone /spawn` - Run on both accounts
- `/stats Account1` - Get stats

That's it! 1 jar, 1 webhook, 1 bot, 2 accounts.
