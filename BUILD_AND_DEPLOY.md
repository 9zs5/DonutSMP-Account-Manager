# BUILD AND DEPLOY GUIDE

## What You Have

✓ One Fabric mod (Java)
✓ One Discord bot (Python)
✓ One hardcoded webhook
✓ ! command prefix
✓ No passwords stored anywhere

## Step 1: Build the Jar

On your PC with Java 21 installed:

```bash
cd DonutSMP-Account-Manager
./gradlew build
```

This creates: `build/libs/donutsmp-account-manager-1.0.0.jar`

## Step 2: Install on Your Minecraft PC

1. Install Fabric Loader (if you don't have it): https://fabricmc.net/
2. Put the jar in: `.minecraft/mods/`
3. Launch Minecraft
4. Connect to donutsmp.net
5. You should see a message in Discord saying you connected

## Step 3: Set Up and Run the Discord Bot

### Option A: Run it locally (on your PC)

1. Make sure Python 3.8+ is installed
2. Go to `discord-bot` folder
3. Run: `pip install -r requirements.txt`
4. Create `bot_config.json`:
   ```json
   {
     "bot_token": "PASTE_YOUR_BOT_TOKEN_HERE"
   }
   ```
5. Run: `python bot.py`
6. Keep it running 24/7 for commands to work

### Option B: Host it on a cloud service (recommended for 24/7)

**Replit (Free):**
1. Go to https://replit.com
2. Create new Repl → select Python
3. Upload the `discord-bot` folder contents
4. Add `bot_config.json` with your token
5. Press "Run"
6. Set to run 24/7 (Replit has options for this)

**Other options:**
- Heroku (paid now, was free)
- AWS
- Google Cloud
- Your own VPS
- Just leave your PC running

## Step 4: Get Your Discord Bot Token

1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it
3. Go to "Bot" tab → Click "Add Bot"
4. Under "TOKEN" → Click "Copy"
5. Paste into `bot_config.json`

## Step 5: Test It

1. Launch Minecraft, connect to donutsmp.net
2. Check Discord - you should see your connection message
3. In Discord, type: `!help`
4. Bot responds with available commands
5. Try: `!whoisonline`

## Commands Available

- `!help` - Show commands
- `!whoisonline` - See online players
- `!run everyone /spawn` - Run on all accounts
- `!run username /home` - Run on one account
- `!stats everyone` - Get stats from all
- `!stats username` - Get stats from one

## Sharing With Friends

1. Build the jar (same jar every time)
2. Share `build/libs/donutsmp-account-manager-1.0.0.jar` with your friends
3. They install it in their `.minecraft/mods/`
4. When they connect to donutsmp.net, they appear in Discord
5. You can command them with `!run username /command`

## Important Notes

✓ Webhook is hardcoded - no setup needed for friends
✓ Only works on donutsmp.net (other servers = offline)
✓ NO passwords stored anywhere
✓ NO account theft
✓ Only reports usernames and server status
✓ One jar for everyone
✓ One bot to run 24/7
✓ Prefix: !

## Troubleshooting

**Jar won't build:**
- Make sure Java 21 is installed: `java -version`
- Make sure Gradle is installed
- Delete `build` folder and try again

**Mod not sending messages:**
- Make sure you're connected to donutsmp.net
- Make sure Discord bot is running
- Check bot console for errors

**Bot won't start:**
- Make sure Python 3.8+ is installed
- Make sure you edited `bot_config.json`
- Make sure bot token is correct
- Check Discord Developer Portal that bot is in your server

**Friends can't connect:**
- Share the same jar file
- Make sure they have Fabric Loader
- Make sure they're connecting to donutsmp.net

## Summary

You now have:
1. A Minecraft mod that reports connections to Discord
2. A Discord bot that handles commands
3. A shared webhook for all users
4. One jar to share with friends
5. No passwords or secrets stored anywhere

The mod and bot automatically work together through the hardcoded webhook.
